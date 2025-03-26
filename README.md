# Cloudflare Rule Generator

This project generates a Cloudflare WAF rule using regular expressions based on an input list of full URLs and HTTP methods.

## Usage

1. Create or edit `api.txt` to include your API rules, one per line:
   ```
   https://example.com/api,GET
   https://example.com/login
   ```

2. Run the script:
   ```bash
   python generate_rule.py api.txt
   ```

3. The output will be a Cloudflare rule that can be used in WAF settings.

## Example Output

```
(http.request.full_uri matches "https://example.com/api" and http.request.method eq "GET") or (http.request.full_uri matches "https://example.com/login")
```

## License

MIT
