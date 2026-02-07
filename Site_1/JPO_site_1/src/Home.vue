<template>
  <div class="page">
    <div class="login-box">
      <h1>Authentification</h1>
      <p class="subtitle">
        Accès (pas trop) sécurisé à la plateforme
      </p>

      <form @submit.prevent="login">
        <input
          v-model="username"
          type="text"
          placeholder="Nom d'utilisateur"
          required
        />

        <input
          v-model="mdp"
          type="text"
          placeholder="Mot de passe"
          required
        />

        <button type="submit">
          Se connecter
        </button>
      </form>

      <div class="message success" v-if="success">
        Connexion réussie
      </div>

      <div class="message error" v-if="error">
        Identifiants incorrects
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      username: "",
      mdp: "",
      success: false,
      error: false,
    };
  },
  methods: {
    async login() {
      this.success = false;
      this.error = false;

      try {
        // Envoi POST avec payload JSON
        const response = await axios.post(
          "http://localhost:8000/user", 
          {
            username: this.username,
            mdp: this.mdp
          }
        );

        if (response.data === true) {

          this.$router.push({
        path: '/connected',
        query: {
          username: this.username,
        }
        })
        } else {
          this.error = true;
        }
      } catch (e) {
        console.error(e);
        this.error = true;
      }
    },
  },
};

</script>


<style scoped>
.page {
  width: 100vw;
  height: 100vh;
  background: radial-gradient(circle at top, #1e293b, #020617);
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}

.login-box {
  width: 380px;
  background: rgba(15, 23, 42, 0.95);
  padding: 3rem;
  border-radius: 14px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
  text-align: center;
}

.login-box h1 {
  margin-bottom: 0.3rem;
  font-size: 1.8rem;
}

.subtitle {
  font-size: 0.9rem;
  opacity: 0.7;
  margin-bottom: 2rem;
}

input {
  width: 100%;
  padding: 0.9rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  border: none;
  outline: none;
  font-size: 1rem;
}

button {
  width: 100%;
  padding: 0.9rem;
  border-radius: 8px;
  border: none;
  background: #2563eb;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s ease;
}

button:hover {
  background: #1d4ed8;
}

.message {
  margin-top: 1.5rem;
  font-weight: bold;
}

.success {
  color: #22c55e;
}

.error {
  color: #ef4444;
}
</style>
