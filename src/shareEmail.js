/**
 * Recipient for in-app "Share on Email" (mailto). Not the logged-in user's address.
 */
export const SHARE_ON_EMAIL_TO = 'MatchMyTone <noreply@matchmytone.online>';

/** URL-encoded for use in mailto: paths, e.g. `mailto:${SHARE_ON_EMAIL_TO_ENCODED}?subject=...` */
export const SHARE_ON_EMAIL_TO_ENCODED = encodeURIComponent(SHARE_ON_EMAIL_TO);
