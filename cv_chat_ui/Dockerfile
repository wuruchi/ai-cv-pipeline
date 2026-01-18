FROM node:24-alpine
# Set working directory
WORKDIR /app
# Copy package files
COPY package.json package-lock.json /app/
# Install dependencies
RUN npm install
# Expose port
EXPOSE 3000
COPY . /app/
# Start the development server
CMD ["npm", "run", "dev"]