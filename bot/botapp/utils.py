import os
import pdfkit
from django.conf import settings

def letter(letter_elements, fileName):
    output_path = os.path.join(settings.MEDIA_ROOT, fileName)

    html_content = """
    <html>
    <head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 800px;
            background-color: #fff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        .header {
            background-color: #1a202c;
            color: #fff;
            padding: 20px;
            display: flex;
            flex-direction:row;
            
            justify-content: space-between;
            align-items: center;
        }
        .header .company-details {
            display: flex;
            align-items: center;
        }
        .header .company-details h3 {
            margin: 0;
            font-size: 1.25rem;
        }
        .header .company-details p {
            margin: 0;
            font-size: 0.875rem;
            color: #e2e8f0;
        }
        .header .contact-info {
            text-align: right;
        }
        .header .contact-info p {
            margin: 0;
            font-size: 0.875rem;
            color: #e2e8f0;
        }
        .bodyy {
            padding: 40px;
            color: #4a5568;
        }
        .bodyy h2 {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .bodyy p {
            margin: 0;
            margin-top: 1rem;
            line-height: 1.6;
        }
        .footer {
            background-color: #edf2f7;
            color: #4a5568;
            text-align: center;
            padding: 20px;
            font-size: 0.875rem;
        }
    </style>
    </head>
    <body>
    <div class="container">
    """

    for item in letter_elements:
        html_content += f"""
        <div class="section">
            <div class="header">
                <div class="company-details">
                    <h3>{item.CompanyName}</h3>
                    <p>{item.CompanyAddress}</p>
                </div>
                <div class="contact-info">
                    <p>Tel: {item.CompanyPhone}</p>
                    <p>Email: {item.CompanyEmail}</p>
                </div>
            </div>
            <div class="bodyy">
                <h2>{item.Header}</h2>
                <p>{item.Body}</p>
                <p>Sincerely,</p>
                <p>{item.Footer}</p>
            </div>
            <div class="footer">
                &copy; 2024 {item.CompanyName}. All rights reserved.
            </div>
        </div>
        """

    html_content += """
    </div>
    </body>
    </html>
    """

    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    pdfkit.from_string(html_content, output_path, configuration=config)

    return fileName
