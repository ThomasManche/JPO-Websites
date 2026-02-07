<template>
  <div class="page">
    <div class="main-card">
      <!-- Logos -->
      <div class="logos">
        <img
          src="https://upload.wikimedia.org/wikipedia/fr/thumb/7/72/2560px-Insa-hautsdefrance-logo.png/330px-2560px-Insa-hautsdefrance-logo.png"
          alt="INSA HdF"
        />
        <img
          src="https://www.uphf.fr/sites/default/files/media/2021-12/uphf-logo.svg"
          alt="UPHF"
        />
      </div>

      <!-- Contenu principal -->
      <h1>Bienvenue à l'INSA Hauts-de-France 🎓</h1>

      <h2>
        Spécialité :
        <strong>Informatique & Cybersécurité</strong>
      </h2>

      <div class="divider"></div>

      <p class="welcome">
        Bienvenue <span class="user">{{ username }}</span>,
        vous avez réussi à vous connecter.
      </p>

      <p class="warning">
        HTTPs est un protocole <strong>sécurisé</strong>,
        vos données sont chiffrés durant l'envoi. Aucune personne ne peut vous voler vos données facilement !
      </p>

      <!-- Carrousel -->
      <h3 class="carousel-title">Exemples de cours Cyber</h3>

      <div class="carousel">
        <button class="arrow left" @click="prevSlide">‹</button>

        <div
          class="slide"
          :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
        >
          <div
            class="course-card"
            v-for="(course, i) in courses"
            :key="i"
          >
            <div
              class="bg"
              :style="{ backgroundImage: `url(${course.image})` }"
            ></div>
            <div class="text">
              <h4>{{ course.name }}</h4>
              <p>{{ course.desc }}</p>
            </div>
          </div>
        </div>

        <button class="arrow right" @click="nextSlide">›</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      currentIndex: 0,
      courses: [
        {
          name: "Cryptographie",
          desc: "RSA, SHA, hachage, cryptographie avancée et post-quantique",
          image:
            "https://images.unsplash.com/photo-1639322537228-f710d846310a"
        },
        {
          name: "RGPD",
          desc: "Droits sur les données personnelles et critères de sensibilité",
          image:
            "https://images.unsplash.com/photo-1589829545856-d10d557cf95f"
        },
        {
          name: "Détection et réponse aux incidents",
          desc: "SOC, SIEM, analyse d’attaques et réponse aux incidents",
          image:
            "https://images.unsplash.com/photo-1600267175161-cfaa711b4a81"
        },
        {
          name: "Sécurité des objets connectés & du Cloud",
          desc: "Sécurisation IoT, Cloud, API et architectures distribuées",
          image:
            "https://images.unsplash.com/photo-1518770660439-4636190af475"
        },
        {
          name: "Gestion des identités",
          desc: "             IAM, authentification forte, RBAC, SSO",
          image:
            "https://images.unsplash.com/photo-1556740749-887f6717d7e4"
        },
        {
          name: "Sécurité applicative",
          desc: "OWASP, failles web, tests d’intrusion et revue de code",
          image:
            "https://www.redopus.fr/sites/redopus.fr/files/Composantes_de_la_securite_applicative.jpg"
        }
      ]
    };
  },
  methods: {
    prevSlide() {
      this.currentIndex =
        (this.currentIndex - 1 + this.courses.length) % this.courses.length;
    },
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.courses.length;
    }
  },
  async mounted() {
    try {
      const res = await axios.get("https://localhost:8001/me", {
        withCredentials: true
      });
      this.username = res.data.username;
    } catch {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
.page {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: Arial, sans-serif;
}

.main-card {
  background: white;
  width: 900px;
  padding: 2rem 3rem 3rem;
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
  position: relative;
}

/* Logos */
.logos {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.logos img {
  height: 55px;
}

/* Textes */
h1 {
  color: #203a43;
}

h2 {
  color: #2c5364;
}

.divider {
  width: 80px;
  height: 3px;
  background: #2c5364;
  margin: 1rem 0;
  border-radius: 2px;
}

.user {
  font-weight: bold;
  color: #2c5364;
}

.warning {
  background: #fff3cd;
  border-left: 5px solid #ff9800;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

/* Carrousel */
.carousel-title {
  margin-bottom: 1rem;
}

.carousel {
  position: relative;
  overflow: hidden;
  height: 320px;
}

.slide {
  display: flex;
  height: 100%;
  transition: transform 0.45s ease;
}

.course-card {
  min-width: 100%;
  position: relative;
  border-radius: 14px;
  overflow: hidden;
}

.bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: brightness(0.6);
}

.text {
  position: absolute; /* On passe en absolute pour mieux contrôler la zone */
  inset: 0;           /* Remplit toute la carte */
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
  z-index: 1;
  
  /* C'est ici que ça se joue : */
  padding-left: 120px;  /* Largement assez pour dépasser la flèche (10px + 46px) */
  padding-right: 120px; /* Symétrie pour la flèche de droite */
  box-sizing: border-box;
}

.text h4 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

/* Flèches */
.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  background: rgba(32, 58, 67, 0.9);
  color: white;
  border: none;
  width: 46px;
  height: 46px;
  font-size: 1.8rem;
  border-radius: 50%;
  cursor: pointer;
  pointer-events: auto;
}

.arrow.left {
  left: 0px;
}

.arrow.right {

  right: 0px;
}
</style>
