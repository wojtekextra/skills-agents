@echo off
echo.
echo ===== Mock SMTP Server for Testing =====
echo.
echo Starting mock SMTP server on localhost:1025
echo All emails will be printed to console (not actually sent)
echo.
echo Press Ctrl+C to stop the server
echo.

python -m smtpd -c DebuggingServer -n localhost:1025
