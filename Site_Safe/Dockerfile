# ======================
# Étape 1 : Build Vue
# ======================
FROM node:20-alpine AS build

WORKDIR /app

# Copier uniquement le code Vue
COPY JPO_site_safe/package*.json ./
RUN npm install
COPY JPO_site_safe/ ./

RUN npm install axios
RUN npm install vue-router@4
RUN npm run build

# ======================
# Étape 2 : Nginx
# ======================
FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
