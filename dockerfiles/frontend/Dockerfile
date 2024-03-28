FROM node:20.11.1
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ .
EXPOSE 3000
CMD [ "npm", "start"]