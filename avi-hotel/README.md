# Avinash Hotel Website

### Links
- https://smooth-hotel.netlify.app - web app
- https://mren-hotel.herokuapp.com/api/users/register - API



### Notes
- https://www.rapid7.com/blog/post/2019/12/06/hidden-helpers-security-focused-http-headers-to-protect-against-vulnerabilities/
- Header Inspector website - https://headerinspector.com/
- We can see that some of the headers are not configured properly
```
Content-Security-Policy header was not found. You should add the header to control the sources of content on your site.
Referrer-Policy header was not found. Your site should be explicit on how referrer headers are handled.
X-Frame-Options was not found. Your site should be deterministic on how it is framed. Setting this header will help with that.
X-XSS-Protection header was not found. Setting this header will enable your browsers integrated XSS filtering.
X-Content-Type-Options header was not found. This header should be set with the nosniff attribute to prevent your browser from being tricked into executing arbitrary code.
Strict-Transport-Security was not detected. Adding this header will prevent HTTP downgrade attacks.
```
- **Content-Security-Policy** - Without setting this header we can load other information which is not specified in the website
  - dangling markup exploits - https://portswigger.net/web-security/cross-site-scripting/dangling-markup

- https://medium.com/swlh/hacking-the-same-origin-policy-f9f49ad592fc - might be vulnerable to CORS attacks

### Vulnerability
- No limitation for review
