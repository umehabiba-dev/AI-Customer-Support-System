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

if 'ticket_history' not in st.session_state:
    st.session_state.ticket_history = []

st.title("AI Customer Support Agent")
st.markdown("Enter a support ticket below to get a summary and suggested reply.")

ticket_source = st.selectbox("Ticket Source", ["Email", "Chat", "Voice Transcript", "Manual Entry"], help="Select the source type. In a full system, this would determine processing method.")

ticket_text = st.text_area("Support Ticket", height=200, placeholder="Paste the support ticket here...")

col1, col2 = st.columns(2)

with col1:
    process_btn = st.button("Process Ticket", type="primary")

with col2:
    if st.button("Clear History"):
        st.session_state.ticket_history = []
        st.rerun()

if process_btn:
    if not ticket_text.strip():
        st.warning("Please enter a support ticket")
    else:
        with st.spinner("Analyzing ticket..."):
            try:
                context_note = ""
                if st.session_state.ticket_history:
                    recent_tickets = "\n".join([f"- {h['summary']}" for h in st.session_state.ticket_history[-3:]])
                    context_note = f"\n\nRecent similar tickets handled:\n{recent_tickets}\n\nUse patterns from previous tickets to maintain consistency."
                
                summary_prompt = f"""Summarize this customer support ticket in 2-3 sentences. Focus on the main issue and customer sentiment.

Ticket Source: {ticket_source}
Ticket: {ticket_text}
{context_note}
Summary:"""
                
                reply_prompt = f"""Based on this customer support ticket, suggest a professional and helpful reply. Keep it concise (3-4 sentences) and empathetic.

Ticket Source: {ticket_source}
Ticket: {ticket_text}
{context_note}
Suggested Reply:"""
                
                summary_response = client.models.generate_content(model='gemini-3-flash-preview', contents=summary_prompt)
                reply_response = client.models.generate_content(model='gemini-3-flash-preview', contents=reply_prompt)
                
                ticket_data = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'source': ticket_source,
                    'ticket': ticket_text[:100] + "..." if len(ticket_text) > 100 else ticket_text,
                    'summary': summary_response.text,
                    'reply': reply_response.text
                }
                st.session_state.ticket_history.append(ticket_data)
                
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

if st.session_state.ticket_history:
    st.divider()
    st.subheader("Ticket History (Learning from Past Interactions)")
    st.caption("This demonstrates how the system could learn from past tickets. In a full implementation, this would be stored in a database and used to improve responses.")
    
    for i, ticket in enumerate(reversed(st.session_state.ticket_history[-5:]), 1):
        with st.expander(f"Ticket #{len(st.session_state.ticket_history) - i + 1} - {ticket['source']} ({ticket['timestamp']})"):
            st.write(f"**Original Ticket:** {ticket['ticket']}")
            st.write(f"**Summary:** {ticket['summary']}")
            st.write(f"**Reply:** {ticket['reply']}")
