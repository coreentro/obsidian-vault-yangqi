# Antigravity Login Diagnosis

## Evidence gathered on 2026-07-16

- The Antigravity desktop app is running version `2.2.1`.
- The displayed error is: `Sorry, this account is ineligible to use Antigravity` and `Authentication failed`.
- Official Antigravity FAQ states that authentication is currently available only to personal Google accounts in approved geographies; it recommends a `@gmail.com` account when Workspace accounts have issues.
- The official FAQ states that eligibility depends on the country shown on the Google Terms of Service page, not merely the device's network location.
- An unauthenticated Google Terms page shown in the browser displays `国家/地区版本：中国` (Country/region version: China). Because that browser session was not signed in, this does **not** prove the Antigravity account's own country association.
- Current public-network routing is split by destination: one IP geolocation service observed a Los Angeles, United States egress IP, while another observed a China Telecom egress IP in Henan, China.
- Mainland China is not in the Antigravity FAQ's approved geography list.

## Conclusion

The most supported root cause remains a server-side eligibility check, but the specific account-side trigger has not been confirmed. A region mismatch is plausible because the network has destination-specific routing and mainland China is outside the published availability list. Other documented possibilities are account type (Workspace instead of a personal account), age verification, or account enforcement.

## Retry result

On 2026-07-16, the account was authenticated again through Google’s official OAuth flow in Chrome. Google returned an Antigravity authentication-success page, but the Antigravity app immediately returned to the same `account is ineligible` / `Authentication failed` screen. This confirms that the failure happens after Google sign-in, during Antigravity’s own server-side eligibility check.

## Support request

On 2026-07-16, an `Auth and Billing` feedback request was submitted from the linked Google account. It requested the exact eligibility criterion that failed, included the successful-OAuth / failed-Antigravity reproduction steps and the desktop app version (`2.2.1` on macOS), and did not attach a screenshot or Antigravity server logs. The form cleared and its Submit button became disabled after submission; no case number was shown.

## Legitimate next steps

1. If the account is genuinely resident in a supported country/region but Google has the country association wrong, use the official country-association request linked from the FAQ to correct it.
2. Use a personal `@gmail.com` account rather than a Workspace-managed account, if applicable.
3. If age verification is pending, complete it in the Google Account age-verification page; Antigravity requires users to be at least 18.
4. If the account previously used third-party tools/services to access Antigravity, review the product terms and contact official support through the in-app `Having trouble? Let us know` link. The FAQ says this can lead to suspension or termination.

Do not rely on clearing local data or reinstalling as a primary fix: neither changes the account’s server-side eligibility.
