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
        HTTP est un protocole <strong>non sécurisé</strong>,
        vos données sont envoyé clairement, dont votre mot de passe... Toute personne qui écoute le traffic peut le voir !
      </p>

      <!-- Carrousel -->
      <h3 class="carousel-title">Exemples de cours en Informatique & IA</h3>

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
export default {
  props: ['username'],
  data() {
    return {
      currentIndex: 0,
courses: [
  {
    name: "Modèles mathématiques & IA",
    desc: "Logique du premier ordre, Prolog, fondements théoriques de l'IA et méthodes de résolution",
    image: "https://cdn.prod.website-files.com/65cb885e207a8d416674eca1/66a748096aac53884286a97a_IA-9.png"
  },
  {
    name: "Programmation",
    desc: "C, Python, HTML/CSS/JS, Flutter, Java",
    image: "https://images.unsplash.com/photo-1516116216624-53e697fedbea"
  },
  {
    name: "Développement Web",
    desc: "Architecture Front-end & Back-end, communication temps réel avec WebSockets",
    image: "https://images.unsplash.com/photo-1547658719-da2b51169166"
  },
  {
    name: "Networking et Protocoles réseaux",
    desc: "Architecture OSI, TCP/IP, routage et gestion des flux réseaux",
    image: "https://images.unsplash.com/photo-1544197150-b99a580bb7a8"
  },
  {
    name: "Programmation système",
    desc: "Gestion des processus, IPC (pipes, signaux) et interaction bas-niveau avec le noyau",
    image: "https://images.unsplash.com/photo-1629654297299-c8506221ca97"
  },
  {
    name: "Génie logiciel",
    desc: "Conception logicielle, modélisation avec les diagrammes UML et patterns d'architecture",
    image: "https://images.unsplash.com/photo-1531403009284-440f080d1e12"
  },
  {
    name: "Complexité",
    desc: "Analyse algorithmique, classes de complexité, optimalité et calculabilité",
    image: "https://images.unsplash.com/photo-1509228468518-180dd4864904"
  },
  {
    name: "Base de données",
    desc: "Conception de schémas, requêtage SQL avancé et gestion des données transactionnelles",
    image: "https://images.unsplash.com/photo-1544383835-bda2bc66a55d"
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
}
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