FROM node:24-alpine
# Set working directory
WORKDIR /app
# Copy package files
COPY package.json package-lock.json /app/
# Install dependencies
RUN npm install
# Expose port
EXPOSE 8080
# Start the development server
CMD ["npm", "run", "preview"]
