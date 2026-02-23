def run_header_audit(response):
    """Scans headers for missing security configurations."""
    headers = response.headers
    findings = []
    
    if 'Strict-Transport-Security' not in headers:
        findings.append("HSTS Missing")
    if 'X-Frame-Options' not in headers:
        findings.append("X-Frame-Options Missing")
        
    return findings