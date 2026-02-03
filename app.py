import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from datetime import datetime

load_dotenv()

st.set_page_config(page_title="AI Customer Support Agent", page_icon="💬")

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    st.error("Please set GEMINI_API_KEY in .env file")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("AI Customer Support Agent")
st.markdown("Enter a support ticket below to get a summary and suggested reply.")

ticket_text = st.text_area("Support Ticket", height=200, placeholder="Paste the customer support ticket here...")

if st.button("Process Ticket"):
    if not ticket_text.strip():
        st.warning("Please enter a support ticket")
    else:
        with st.spinner("Analyzing ticket..."):
            try:
                summary_prompt = f"""Summarize this customer support ticket in 2-3 sentences. Focus on the main issue and customer sentiment.

Ticket: {ticket_text}

Summary:"""
                
                reply_prompt = f"""Based on this customer support ticket, suggest a professional and helpful reply. Keep it concise (3-4 sentences) and empathetic.

Ticket: {ticket_text}

Suggested Reply:"""
                
                summary_response = client.models.generate_content(model='gemini-3-flash-preview', contents=summary_prompt)
                reply_response = client.models.generate_content(model='gemini-3-flash-preview', contents=reply_prompt)
                
                st.success("Ticket processed successfully!")
                
                st.subheader("Ticket Summary")
                st.write(summary_response.text)
                
                st.subheader("Suggested Reply")
                st.write(reply_response.text)
                
                st.download_button(
                    label="Download Reply",
                    data=reply_response.text,
                    file_name=f"reply_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Error processing ticket: {str(e)}")
                st.info("Make sure your Gemini API key is valid and you're using the free tier.")
