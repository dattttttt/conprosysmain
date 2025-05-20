# frontend/Dockerfile

# Sử dụng Node.js để build Vue.js project
FROM node:18-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .   
RUN npm run build

# Sử dụng Nginx để serve file tĩnh
FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
