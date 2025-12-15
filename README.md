 🚀 Space Defender

**UAS Pemrograman Berorientasi Objek**  
Game sederhana berbasis OOP menggunakan Python dan Pygame

---

## 📋 Deskripsi

Space Defender adalah game arcade shooter 2D dimana pemain mengendalikan pesawat luar angkasa untuk bertahan dari serangan asteroid dan alien enemies. Game ini dikembangkan untuk mendemonstrasikan implementasi prinsip-prinsip Object-Oriented Programming (OOP).

### ✨ Fitur Utama

- 🎮 **Kontrol Responsif**: Movement 8-arah dengan WASD atau Arrow Keys
- 🔫 **Shooting Mechanics**: Sistem tembak dengan cooldown
- 👾 **Multiple Enemy Types**: Asteroid dan UFO dengan behavior berbeda
- 💥 **Collision Detection**: Sistem collision yang akurat
- 📊 **HUD System**: Score counter dan health bar visual
- 🎯 **Progressive Difficulty**: Spawn rate meningkat seiring waktu
- 🎨 **Custom Graphics**: Designed dengan primitive shapes

---

## 🎓 Konsep OOP yang Diimplementasikan

### 1. Encapsulation
- Private attributes menggunakan double underscore (`__`)
- Getter dan Setter methods untuk controlled access
- Data integrity dan validation

### 2. Inheritance
- **Single Inheritance**: Player, Bullet, Enemy extends GameObject
- **Multi-level Inheritance**: Asteroid, FastEnemy extends Enemy extends GameObject
- Code reusability dan hierarchy design

### 3. Polymorphism
- **Method Overriding**: draw(), update(), move() methods
- Runtime polymorphism untuk flexible behavior
- Uniform interface untuk different object types

---

## 🏗️ Struktur Project

```
space_defender/
│
├── main.py              # Entry point & game loop
├── game_object.py       # Base class (Encapsulation)
├── player.py            # Player class (Inheritance)
├── enemy.py             # Enemy classes (Inheritance & Polymorphism)
├── bullet.py            # Bullet class
├── game_manager.py      # Game logic coordinator
├──laporan.pdf
```

---

## 📊 Class Diagram

```
GameObject (Base)
    ├── Player
    ├── Bullet
    └── Enemy
        ├── Asteroid
        └── FastEnemy

GameManager (Coordinator)
    ├── Player (1)
    └── Enemies (0..*)
```

---

## 🎮 Cara Bermain

### Controls

| Action | Key |
|--------|-----|
| Move Up | W / ↑ |
| Move Down | S / ↓ |
| Move Left | A / ← |
| Move Right | D / → |
| Shoot | SPACE |
| Start/Restart | ENTER |
| Quit | ESC |

### Objective

- 🎯 Hancurkan asteroid dan enemy untuk mendapat poin
- ❤️ Jaga health bar agar tidak habis
- 🏆 Raih score setinggi mungkin!

### Enemy Types

- **Asteroid** 🪨
  - Bergerak lurus ke bawah
  - Rotasi saat bergerak
  - Points: 10

- **UFO** 🛸
  - Bergerak zigzag
  - Lebih cepat dari asteroid
  - Points: 20

---

## 🔧 Technical Details

### Technologies Used

- **Language**: Python 3.8+
- **Library**: Pygame 2.5.0+
- **Architecture**: Object-Oriented Programming

### Design Patterns

- **Inheritance Hierarchy**: GameObject sebagai base class
- **Composition**: GameManager contains Player dan Enemies
- **Encapsulation**: Private attributes dengan getter/setter
- **Polymorphism**: Method overriding untuk custom behavior

---

## 📸 Screenshots

### Menu Screen
```
╔══════════════════════════════╗
║      SPACE DEFENDER          ║
║                              ║
║   Press ENTER to Start       ║
║   Arrow Keys/WASD to Move    ║
║   SPACE to Shoot             ║
╚══════════════════════════════╝
```

### Gameplay
```
Score: 180    Health: 60
█████████████████░░░░░░░ [Health Bar]

         △  (Player)
        │││ (Bullets)
    
     🪨  🛸  🪨  (Enemies)
```

---

## 📝 Author

**Graynaldo Fahrul Oktavian Mahendra**  
NIM: 24091397081  
Kelas: 2024 C
Program Studi: Manajemen Informatika  
Universitas: Universitas Negeri Surabaya

---

## 📄 License

This project is created for educational purposes as part of Object-Oriented Programming course assignment.

---

## 🙏 Acknowledgments

- Dosen Pengampu: Bu Rosita
- Pygame Community
- Python Documentation

---

## 📞 Contact

- Email: 24091397081@mhs.unesa.ac.id
- GitHub: github.com/Graynaldoo

---

**Made with ❤️ for UAS PBO**
