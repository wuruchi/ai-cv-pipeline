import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export default class ChatApiClient {

  constructor(apiUrl = API_BASE_URL) {
    this.apiUrl = apiUrl;
  }

  async sendMessage(message) {
    const response = await axios.post(`${this.apiUrl}/chat`, message);
    return response.data;
  }

  async getSource(cvId) {
    const response = await axios.get(`${this.apiUrl}/source/${cvId}`, {
      responseType: 'blob',
    });
    return response.data;
  }
}