# How to View the Error Log in Expo Go

## To See the Actual Error:

1. **In Expo Go app**, tap on **"View error log"** at the bottom of the error screen
2. **Or in the terminal**, look for any red error messages
3. **Or press `j`** in the Expo terminal to open the debugger

## Common Errors and Fixes:

### Error: "Cannot find module"
- **Fix**: Run `npm install` and restart

### Error: "Unable to resolve module"
- **Fix**: Clear cache: `npx expo start --clear`

### Error: "Element type is invalid"
- **Fix**: Check for missing default exports in route files

### Error: "Cannot read property of undefined"
- **Fix**: Check for null/undefined values in your code

## After Viewing Error Log:

**Please share the exact error message** so I can fix it!

The error log will show:
- Which file is causing the problem
- Which line has the error
- What the actual error is

This will help me fix it immediately!



