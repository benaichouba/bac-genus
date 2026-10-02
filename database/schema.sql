:root {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #eaf4ff;
  background: #081824;
  line-height: 1.5;
  font-weight: 400;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  background:
    radial-gradient(circle at top, rgba(52, 127, 201, 0.35), transparent 30%),
    linear-gradient(135deg, #07131d 0%, #0d2236 100%);
}

button, input {
  font: inherit;
}

#root {
  min-height: 100vh;
}

.app-shell {
  max-width: 1300px;
  margin: 0 auto;
  padding: 24px 20px 60px;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  padding: 18px 20px;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(10, 28, 42, 0.7);
  backdrop-filter: blur(10px);
  border-radius: 18px;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-mark {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  background: linear-gradient(135deg, #18b8ff, #254dca);
  font-weight: 800;
  color: white;
}

.topbar h1 {
  margin: 0;
  font-size: 1.8rem;
}

.topbar small {
  color: #9ec2e7;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.nav a {
  color: #dfeefc;
  text-decoration: none;
  font-weight: 600;
}

.layout {
  display: grid;
  gap: 24px;
  margin-top: 24px;
}

.panel {
  background: rgba(11, 27, 38, 0.82);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.hero {
  min-height: 220px;
  display: grid;
  align-items: center;
  background:
    linear-gradient(120deg, rgba(24, 184, 255, 0.15), rgba(41, 92, 167, 0.32)),
    rgba(11, 27, 38, 0.82);
}

.tag {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(24, 184, 255, 0.15);
  border: 1px solid rgba(24, 184, 255, 0.4);
  color: #8edaff;
  margin-bottom: 12px;
}

.hero h2 {
  margin: 0 0 12px;
  font-size: clamp(2rem, 4vw, 3rem);
  line-height: 1.15;
}

.hero p {
  max-width: 720px;
  font-size: 1rem;
  color: #d5e6f7;
}

.section-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.section-head h3 {
  margin: 0;
  font-size: 1.5rem;
}

.lesson-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 14px;
}

.lesson-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.02);
  color: white;
  text-align: left;
  cursor: pointer;
  transition: 0.2s ease;
}

.lesson-item:hover, .lesson-item.active {
  transform: translateY(-2px);
  border-color: rgba(24, 184, 255, 0.8);
  background: rgba(24, 184, 255, 0.08);
}

.lesson-item span {
  color: #bddaf4;
  font-size: 0.92rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

.lesson-view h3 {
  margin-top: 0;
  font-size: 2rem;
}

.lesson-summary {
  color: #98c4e8;
}

.lesson-content {
  white-space: pre-line;
  color: #edf7ff;
  line-height: 1.8;
}

.exercise-list, .prediction-list, .topic-grid {
  display: grid;
  gap: 14px;
}

.exercise-item, .prediction-item, .topic-card {
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 14px 16px;
  background: rgba(255,255,255,0.02);
}

.badge {
  display: inline-block;
  background: rgba(24, 184, 255, 0.14);
  border: 1px solid rgba(24, 184, 255, 0.4);
  color: #8edaff;
  padding: 4px 8px;
  border-radius: 999px;
  margin-bottom: 10px;
  font-size: 0.72rem;
  font-weight: 700;
}

.exercise-item p, .prediction-item p {
  margin: 0;
  color: #dfeefc;
}

.prediction-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}

.prediction-item span {
  font-size: 1.5rem;
  color: #8edaff;
  font-weight: 700;
}

.topic-grid {
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
}

.topic-card strong {
  display: block;
  margin-top: 6px;
  font-size: 1.8rem;
  color: #8edaff;
}

.admin-panel {
  display: grid;
  gap: 16px;
}

.file-label {
  display: grid;
  gap: 8px;
  color: #dfeefc;
}

.file-label input {
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.04);
  color: white;
}

.upload-box {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 90px;
  border: 1px dashed rgba(24,184,255,0.7);
  border-radius: 16px;
  background: rgba(24,184,255,0.04);
  cursor: pointer;
}

.upload-box input {
  display: none;
}

.message {
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(24,184,255,0.1);
  color: #9fe0ff;
}

@media (max-width: 900px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .topbar {
    flex-direction: column;
    align-items: flex-start;
  }
}

