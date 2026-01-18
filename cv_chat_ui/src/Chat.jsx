import react, { useState, useRef, useEffect } from 'react';
import ChatApiClient from './clients/chat-api';
import ReactMarkdown from 'react-markdown';

export const Chat = () => {

    const [messages, setMessages] = useState([]);
    const [responses, setResponses] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [loadingMessage, setLoadingMessage] = useState(false);

    const chatApiClient = new ChatApiClient();
    const responsesRef = useRef(null);  // Ref for the responses section


    useEffect(() => {
        if (responsesRef.current) {
            responsesRef.current.scrollTop = responsesRef.current.scrollHeight;
        }
    }, [responses, messages]);

    const handleSendMessage = async () => {
        if (!inputValue.trim()) return;
        setLoadingMessage(true);
        const userMessage = inputValue.trim();
        setMessages([...messages, userMessage]);
        setInputValue('');

        try {
            const response = await chatApiClient.sendMessage({ message: userMessage });
            setResponses([...responses, response]);

        } catch (error) {
            console.error('Error sending message:', error);
            setResponses([...responses, 'Error: Unable to get response from server.']);
        }
        setLoadingMessage(false);
    }

    const handleOpenPdf = async (cvId) => {
        try {
            const pdfBlob = await chatApiClient.getSource(cvId);
            const pdfUrl = URL.createObjectURL(pdfBlob);
            window.open(pdfUrl, '_blank');
        } catch (error) {
            console.error('Error fetching PDF source:', error);
        }
    }

    return (
        <section className='chat'>
            <h2 className='chat__title'>CV Chat UI</h2>
            <section className="chat__responses" ref={responsesRef}>
                {responses.map((resp, index) => (
                    <div key={index} className='chat__response'>
                        <ReactMarkdown>{resp.reply}</ReactMarkdown>
                        <div className='chat__response__sources'>
                            <h4>Sources:</h4>
                            <ul className='chat__response__sources__list'>
                                {resp.sources.map((source, srcIndex) => (
                                    <li 
                                        className='chat__response__sources__list__item' 
                                        key={srcIndex} 
                                        onClick={() => handleOpenPdf(source.cvId)}
                                    >
                                        {source.cvId}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>
                ))}
            </section>
            <section className='chat__history'>
                {(messages.reverse()).map((msg, index) => (
                    <div key={index} className='chat__history__message'>
                        {msg}
                    </div>
                ))}
            </section>
            <section className='chat__input'>
                <textarea className="chat__input-field"  placeholder='Type your message here...' value={inputValue} onChange={(e) => setInputValue(e.target.value)} onKeyDown={(e) => {
                    if (e.key === 'Enter') {
                        if (!loadingMessage) handleSendMessage();
                    }
                }} />
                <button className="chat__send-button" onClick={handleSendMessage} disabled={loadingMessage}>
                    {loadingMessage ? 'Sending...' : 'Send'}
                </button>
            </section>
        </section>
    )
}