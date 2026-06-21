#!/usr/bin/env python
"""
Simple mock SMTP server for testing email functionality.
Prints all emails to console instead of sending them.
"""

import asyncio
from aiosmtpd.controller import Controller


class DebugHandler:
    async def handle_DATA(self, server, session, envelope):
        print("=" * 60)
        print("EMAIL RECEIVED")
        print("=" * 60)
        print(f"From: {envelope.mail_from}")
        print(f"To: {envelope.rcpt_tos}")
        print(f"Subject: {envelope.get('subject', 'N/A')}")
        print("-" * 60)
        print(envelope.get_payload(decode=True).decode('utf-8', errors='ignore'))
        print("=" * 60)
        return '250 Message accepted'


if __name__ == "__main__":
    print()
    print("===== Mock SMTP Server for Testing =====")
    print()
    print("Starting mock SMTP server on localhost:1025")
    print("All emails will be printed to console (not actually sent)")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    
    handler = DebugHandler()
    controller = Controller(handler, hostname="localhost", port=1025)
    
    try:
        controller.start()
        print("Server is running...")
        asyncio.run(asyncio.sleep(float('inf')))
    except KeyboardInterrupt:
        print("\nShutting down...")
        controller.stop()
