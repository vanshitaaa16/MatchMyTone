import { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView, Dimensions } from 'react-native';
import { useRouter, useFocusEffect } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { quizAPI } from '../src/api';
import { useCallback } from 'react';

const { width, height } = Dimensions.get('window');

export default function DashboardScreen() {
  const router = useRouter();
  const [resultsExpanded, setResultsExpanded] = useState(false);
  const [quizResults, setQuizResults] = useState({
    skincare: null,
    body_shape: null,
    face_shape: null,
    color_analysis: null
  });
  const [quizData, setQuizData] = useState({
    skincare: null,
    body_shape: null,
    face_shape: null,
  });
  const [loading, setLoading] = useState(true);
  const [errorMessages, setErrorMessages] = useState({
    skincare: '',
    body_shape: '',
    face_shape: '',
    color_analysis: ''
  });

  useEffect(() => {
    fetchQuizResults();
  }, []);

  // Refresh results when screen comes into focus (after taking a quiz)
  useFocusEffect(
    useCallback(() => {
      fetchQuizResults();
    }, [])
  );

  const fetchQuizResults = async () => {
    try {
      setLoading(true);
      const response = await quizAPI.getAllResults();
      if (response && response.results) {
        setQuizResults({
          skincare: response.results.skincare?.result || null,
          body_shape: response.results.body_shape?.result || null,
          face_shape: response.results.face_shape?.result || null,
          color_analysis: null // Color analysis not implemented yet
        });
        // Store full data including answers for navigation
        setQuizData({
          skincare: response.results.skincare || null,
          body_shape: response.results.body_shape || null,
          face_shape: response.results.face_shape || null,
        });
      }
    } catch (error) {
      console.error('Error fetching quiz results:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleResultsClick = () => {
    setResultsExpanded(!resultsExpanded);
  };

  const handleSeeResults = (quizType) => {
    // Clear previous error for this quiz type
    setErrorMessages(prev => ({ ...prev, [quizType]: '' }));

    // Check if quiz result exists
    let hasResult = false;
    let route = '';
    let answers = null;

    switch(quizType) {
      case 'skincare':
        hasResult = quizResults.skincare !== null;
        route = '/SkincareAnalysis/result';
        answers = quizData.skincare?.answers || null;
        break;
      case 'body_shape':
        hasResult = quizResults.body_shape !== null;
        route = '/BodyShapeQuizNew/result';
        answers = quizData.body_shape?.answers || null;
        break;
      case 'face_shape':
        hasResult = quizResults.face_shape !== null;
        route = '/FaceShapeNew/result';
        answers = quizData.face_shape?.answers || null;
        break;
      case 'color_analysis':
        hasResult = false; // Not implemented yet
        route = '';
        break;
    }

    if (!hasResult) {
      setErrorMessages(prev => ({ ...prev, [quizType]: 'Take the quiz first' }));
      return;
    }

    // Navigate to result screen with answers
    if (route && answers) {
      console.log(`Navigating to ${route} with answers:`, answers);
      router.push({
        pathname: route,
        params: { answers: JSON.stringify(answers) }
      });
    } else if (route) {
      // Fallback: navigate without answers (result screen should handle this)
      console.log(`Navigating to ${route} without answers`);
      router.push(route);
    } else {
      console.error('No route or answers found for quiz type:', quizType);
    }
  };

  const handleBack = () => {
    router.push('/home');
  };

  return (
    <LinearGradient colors={['#fffaf3', '#fbeed9']} style={styles.bg}>
      {/* Soft Grid Pattern */}
      <View style={styles.gridOverlay} pointerEvents="none">
        {Array.from({ length: Math.ceil(height / 40) }).map((_, i) => (
          <View key={`h-${i}`} style={[styles.gridLine, styles.gridLineHorizontal, { top: i * 40 }]} />
        ))}
        {Array.from({ length: Math.ceil(width / 40) }).map((_, i) => (
          <View key={`v-${i}`} style={[styles.gridLine, styles.gridLineVertical, { left: i * 40 }]} />
        ))}
      </View>
      <SafeAreaView style={styles.safe}>
        <View style={styles.container}>
          <View style={{ height: 40 }} />

          <View style={styles.headerContainer}>
            <TouchableOpacity
              onPress={handleBack}
              style={styles.backButton}
            >
              <Ionicons name="chevron-forward" size={24} color="#2C2C2C" />
            </TouchableOpacity>
            <Text style={styles.headerTitle}>Dashboard</Text>
          </View>

          <ScrollView 
            style={styles.scrollView}
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
          >
            <View style={styles.card}>
              <View style={styles.optionsContainer}>
              {/* Results Option */}
              <View style={styles.optionSection}>
                <TouchableOpacity 
                  style={styles.mainOption} 
                  onPress={handleResultsClick}
                  activeOpacity={0.6}
                >
                  <Text style={styles.optionText}>RESULTS</Text>
                  <Ionicons 
                    name={resultsExpanded ? "chevron-up" : "chevron-down"} 
                    size={22} 
                    color="#2C2C2C" 
                  />
                </TouchableOpacity>
                <View style={styles.divider} />

                {/* Sub-options that appear when Results is expanded */}
                {resultsExpanded && (
                  <View style={styles.subOptionsContainer}>
                    {/* Color Analysis */}
                    <View style={styles.resultItem}>
                      <View style={styles.resultRow}>
                        <Text style={styles.resultLabel}>Color Analysis:</Text>
                        <Text style={styles.resultValue}>-</Text>
                      </View>
                      <TouchableOpacity 
                        style={styles.seeResultsButton}
                        onPress={() => handleSeeResults('color_analysis')}
                        activeOpacity={0.6}
                      >
                        <Text style={styles.seeResultsButtonText}>See Results</Text>
                      </TouchableOpacity>
                      {errorMessages.color_analysis ? (
                        <Text style={styles.errorText}>{errorMessages.color_analysis}</Text>
                      ) : null}
                    </View>

                    {/* Skincare Analysis */}
                    <View style={styles.resultItem}>
                      <View style={styles.resultRow}>
                        <Text style={styles.resultLabel}>Skincare Analysis:</Text>
                        <Text style={styles.resultValue}>
                          {loading ? 'Loading...' : (quizResults.skincare || '-')}
                        </Text>
                      </View>
                      <TouchableOpacity 
                        style={styles.seeResultsButton}
                        onPress={() => handleSeeResults('skincare')}
                        activeOpacity={0.6}
                      >
                        <Text style={styles.seeResultsButtonText}>See Results</Text>
                      </TouchableOpacity>
                      {errorMessages.skincare ? (
                        <Text style={styles.errorText}>{errorMessages.skincare}</Text>
                      ) : null}
                    </View>

                    {/* Body Analysis */}
                    <View style={styles.resultItem}>
                      <View style={styles.resultRow}>
                        <Text style={styles.resultLabel}>Body Analysis:</Text>
                        <Text style={styles.resultValue}>
                          {loading ? 'Loading...' : (quizResults.body_shape || '-')}
                        </Text>
                      </View>
                      <TouchableOpacity 
                        style={styles.seeResultsButton}
                        onPress={() => handleSeeResults('body_shape')}
                        activeOpacity={0.6}
                      >
                        <Text style={styles.seeResultsButtonText}>See Results</Text>
                      </TouchableOpacity>
                      {errorMessages.body_shape ? (
                        <Text style={styles.errorText}>{errorMessages.body_shape}</Text>
                      ) : null}
                    </View>

                    {/* Face Analysis */}
                    <View style={styles.resultItem}>
                      <View style={styles.resultRow}>
                        <Text style={styles.resultLabel}>Face Analysis:</Text>
                        <Text style={styles.resultValue}>
                          {loading ? 'Loading...' : (quizResults.face_shape || '-')}
                        </Text>
                      </View>
                      <TouchableOpacity 
                        style={styles.seeResultsButton}
                        onPress={() => handleSeeResults('face_shape')}
                        activeOpacity={0.6}
                      >
                        <Text style={styles.seeResultsButtonText}>See Results</Text>
                      </TouchableOpacity>
                      {errorMessages.face_shape ? (
                        <Text style={styles.errorText}>{errorMessages.face_shape}</Text>
                      ) : null}
                    </View>
                  </View>
                )}
              </View>

              {/* About Us Option - appears below Results (and its sub-options if expanded) */}
              <View style={styles.optionSection}>
                <TouchableOpacity 
                  style={styles.mainOption}
                  onPress={() => router.push('/about')}
                  activeOpacity={0.6}
                >
                  <Text style={styles.optionText}>ABOUT US</Text>
                </TouchableOpacity>
                <View style={styles.divider} />
              </View>
            </View>
            </View>
          </ScrollView>
        </View>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  bg: {
    flex: 1,
  },
  safe: { 
    flex: 1, 
    backgroundColor: "#FFF8E7" 
  },
  container: { 
    flex: 1, 
    padding: 20 
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    paddingBottom: 20,
  },
  headerContainer: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 12,
  },
  backButton: {
    padding: 8,
    marginRight: 8,
  },
  headerTitle: { 
    fontSize: 23, 
    fontWeight: "700", 
    color: "#2C2C2C" 
  },
  card: {
    backgroundColor: "#FFFFFF",
    borderRadius: 14,
    padding: 18,
    shadowColor: "#000",
    shadowOpacity: 0.06,
    shadowRadius: 12,
    elevation: 2,
  },
  optionsContainer: {
    gap: 24,
  },
  optionSection: {
    marginBottom: 0,
  },
  mainOption: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 16,
    paddingHorizontal: 4,
  },
  optionText: {
    color: '#2C2C2C',
    fontSize: 20,
    fontWeight: '600',
    letterSpacing: 0.3,
  },
  divider: {
    height: 1,
    backgroundColor: 'rgba(184, 144, 24, 0.2)',
    marginLeft: 4,
  },
  subOptionsContainer: {
    marginTop: 8,
    marginLeft: 24,
    gap: 16,
    paddingVertical: 8,
  },
  resultItem: {
    marginBottom: 12,
  },
  resultRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  resultLabel: {
    color: '#5a4a3a',
    fontSize: 18,
    fontWeight: '500',
    letterSpacing: 0.2,
    marginRight: 8,
  },
  resultValue: {
    color: '#2C2C2C',
    fontSize: 18,
    fontWeight: '600',
  },
  seeResultsButton: {
    backgroundColor: '#b89018',
    paddingVertical: 10,
    paddingHorizontal: 16,
    borderRadius: 8,
    alignSelf: 'flex-start',
    marginTop: 4,
  },
  seeResultsButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  errorText: {
    color: '#ff0000',
    fontSize: 14,
    marginTop: 4,
    fontWeight: '500',
  },
  gridOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    zIndex: 1,
  },
  gridLine: {
    position: 'absolute',
    backgroundColor: 'rgba(184, 144, 24, 0.08)',
  },
  gridLineHorizontal: {
    width: '100%',
    height: 1,
  },
  gridLineVertical: {
    height: '100%',
    width: 1,
  },
});


