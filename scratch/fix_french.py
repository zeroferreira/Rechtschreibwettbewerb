# -*- coding: utf-8 -*-
import os

app_path = "/Users/zeroferreira/Documents/Material English/Spelling 2026/French/js/app.js"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# ----------------- REEMPLAZAR INSTRUCTIONS SCREEN -----------------
start_inst = content.find("const InstructionsScreen = () => {")
end_inst = content.find("const WinnersScreen = () => {")

if start_inst == -1 or end_inst == -1:
    print("Error: No se pudo encontrar InstructionsScreen o WinnersScreen!")
    exit(1)

instructions_code = """const InstructionsScreen = () => {
        const [expandedSection, setExpandedSection] = useState(null);

        const toggleSection = (sect) => {
          setExpandedSection(expandedSection === sect ? null : sect);
        };

        return React.createElement('div', { className: 'min-h-screen p-4 sm:p-8 flex items-center justify-center' },
          React.createElement('div', { className: 'max-w-5xl w-full bg-black bg-opacity-40 backdrop-blur-xl rounded-3xl p-6 sm:p-10 shadow-2xl border border-white border-opacity-15 relative min-h-[500px] flex flex-col md:flex-row gap-8 animate-fadeIn' },
            
            React.createElement('button', {
              onClick: () => setCurrentScreen('home'),
              className: 'absolute top-4 left-4 bg-black text-yellow-400 p-2 sm:p-3 rounded-full hover:bg-yellow-600 hover:text-black transition-all duration-300 shadow-lg transform hover:scale-110 z-10 border border-white/10'
            }, React.createElement(ArrowLeft, { className: 'w-5 h-5 sm:w-6 sm:h-6' })),

            // Panel gauche: Sélecteur de badges hexagonaux
            React.createElement('div', { className: 'w-full md:w-48 flex flex-row md:flex-col justify-center items-center gap-4 mt-8 md:mt-0 flex-wrap' },
              
              // Hexagone 1: Objectif
              React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
                React.createElement('button', {
                  onClick: () => toggleSection('objective'),
                  className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                    expandedSection === 'objective' ? 'bg-green-500 text-black border-green-600' : ''
                  }`,
                  style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
                }, 
                  React.createElement('div', { className: 'text-2xl mb-1' }, '🎯'),
                  React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Objectif')
                )
              ),

              // Hexagone 2: Niveaux
              React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
                React.createElement('button', {
                  onClick: () => toggleSection('levels'),
                  className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                    expandedSection === 'levels' ? 'bg-green-500 text-black border-green-600' : ''
                  }`,
                  style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
                }, 
                  React.createElement('div', { className: 'text-2xl mb-1' }, '📚'),
                  React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Niveaux')
                )
              ),

              // Hexagone 3: Modes
              React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
                React.createElement('button', {
                  onClick: () => toggleSection('modes'),
                  className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                    expandedSection === 'modes' ? 'bg-green-500 text-black border-green-600' : ''
                  }`,
                  style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
                }, 
                  React.createElement('div', { className: 'text-2xl mb-1' }, '🎮'),
                  React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Modes')
                )
              ),

              // Hexagone 4: Règles
              React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
                React.createElement('button', {
                  onClick: () => toggleSection('howToPlay'),
                  className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                    expandedSection === 'howToPlay' ? 'bg-green-500 text-black border-green-600' : ''
                  }`,
                  style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
                }, 
                  React.createElement('div', { className: 'text-2xl mb-1' }, '🎲'),
                  React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Règles')
                )
              ),

              // Hexagone 5: Détails
              React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
                React.createElement('button', {
                  onClick: () => toggleSection('features'),
                  className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                    expandedSection === 'features' ? 'bg-green-500 text-black border-green-600' : ''
                  }`,
                  style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
                }, 
                  React.createElement('div', { className: 'text-2xl mb-1' }, '🔧'),
                  React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Détails')
                )
              )

            ),

            // Panel droit: Contenu détaillé étendu
            React.createElement('div', { className: 'flex-1 mt-6 md:mt-8' },
              !expandedSection && React.createElement('div', { className: 'flex items-center justify-center h-full text-center' },
                React.createElement('div', null,
                  React.createElement('div', { className: 'text-6xl mb-4 animate-bounce' }, '🐝'),
                  React.createElement('h3', { className: 'text-2xl font-black text-white mb-2' }, 'Choisissez une section'),
                  React.createElement('p', { className: 'text-gray-300 font-semibold' }, 'Cliquez sur un hexagone à gauche pour afficher les détails.')
                )
              ),

              expandedSection === 'objective' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
                React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                  React.createElement('span', null, '🎯'), 'Objectif du jeu'
                ),
                React.createElement('p', { className: 'text-gray-200 leading-relaxed font-semibold text-base sm:text-lg' },
                  "L'objectif de ce jeu est de renforcer vos compétences en orthographe française de manière ludique. En écoutant la prononciation et en écrivant l'orthographe correcte, vous améliorez votre intuition linguistique et votre compréhension des mots."
                )
              ),

              expandedSection === 'levels' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
                React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                  React.createElement('span', null, '📚'), 'Niveaux disponibles'
                ),
                React.createElement('ul', { className: 'space-y-4 font-semibold text-gray-200 text-sm sm:text-base' },
                  React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                    React.createElement('span', { className: 'w-4 h-4 bg-emerald-500 rounded-full mr-3 mt-1' }),
                    React.createElement('div', null,
                      React.createElement('strong', { className: 'text-yellow-400' }, 'Niveau A : '), 'A1, A2, KET - Mots de base'
                    )
                  ),
                  React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                    React.createElement('span', { className: 'w-4 h-4 bg-blue-500 rounded-full mr-3 mt-1' }),
                    React.createElement('div', null,
                      React.createElement('strong', { className: 'text-yellow-400' }, 'Niveau B : '), 'B1, B1+, PET - Mots intermédiaires'
                    )
                  ),
                  React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                    React.createElement('span', { className: 'w-4 h-4 bg-purple-500 rounded-full mr-3 mt-1' }),
                    React.createElement('div', null,
                      React.createElement('strong', { className: 'text-yellow-400' }, 'Niveau C : '), 'B2, C1, C2, FC, CAE - Mots avancés'
                    )
                  )
                )
              ),

              expandedSection === 'modes' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
                React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                  React.createElement('span', null, '🎮'), 'Modes de jeu'
                ),
                React.createElement('ul', { className: 'space-y-4 font-semibold text-gray-200 text-sm sm:text-base' },
                  React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                    React.createElement('span', { className: 'w-4 h-4 bg-emerald-500 rounded-full mr-3 mt-1' }),
                    React.createElement('div', null,
                      React.createElement('strong', { className: 'text-yellow-400' }, 'Concours : '), "Jouez contre la montre (30 secondes) avec un maximum de 3 vies."
                    )
                  ),
                  React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                    React.createElement('span', { className: 'w-4 h-4 bg-blue-500 rounded-full mr-3 mt-1' }),
                    React.createElement('div', null,
                      React.createElement('strong', { className: 'text-yellow-400' }, 'Entraînement : '), "Pratiquez librement et sans limite de temps, avec définitions et phrases d'exemple."
                    )
                  )
                )
              ),

              expandedSection === 'howToPlay' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn overflow-y-auto max-h-[380px]' },
                React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                  React.createElement('span', null, '🎲'), 'Comment jouer'
                ),
                React.createElement('ol', { className: 'space-y-3 font-semibold text-gray-200 text-sm sm:text-base list-decimal pl-4' },
                  React.createElement('li', null, 'Sélectionnez votre niveau de difficulté (A, B ou C).'),
                  React.createElement('li', null, 'Choisissez le mode de jeu (Concours ou Entraînement).'),
                  React.createElement('li', null, 'Écoutez le mot en appuyant sur le bouton de prononciation.'),
                  React.createElement('li', null, "Saisissez l'orthographe correcte dans la zone de texte (ou utilisez le micro pour épeler)."),
                  React.createElement('li', null, "Consultez les aides (définitions, exemples) en mode Entraînement."),
                  React.createElement('li', null, 'Appuyez sur valider pour soumettre votre réponse.')
                )
              ),

              expandedSection === 'features' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
                React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                  React.createElement('span', null, '🔧'), 'Fonctionnalités'
                ),
                React.createElement('ul', { className: 'space-y-2.5 font-semibold text-gray-200 text-sm sm:text-base' },
                  React.createElement('li', null, '• Synthèse vocale native avec support des accents de qualité premium.'),
                  React.createElement('li', null, '• Reconnaissance vocale avancée avec transcription instantanée.'),
                  React.createElement('li', null, '• Mode Jour / Nuit dynamique avec persistance automatique de vos préférences.'),
                  React.createElement('li', null, '• Exportation de vos listes de vocabulaire et scores en format CSV.'),
                  React.createElement('li', null, '• Interface premium basée sur le design Glassmorphism hautement réactif.')
                )
              )
            )

          )
        );
      };\n\n      """

content = content[:start_inst] + instructions_code + content[end_inst:]

# Re-read index values because content length has shifted
# ----------------- REEMPLAZAR WINNERS SCREEN -----------------
content_for_winners = content
start_win = content_for_winners.find("const WinnersScreen = () => {")
end_win = content_for_winners.find("const WordListScreen = () => {")

if start_win == -1 or end_win == -1:
    print("Error: No se pudo encontrar WinnersScreen o WordListScreen!")
    exit(1)

winners_code = """const WinnersScreen = () => {
        const [selectedWinner, setSelectedWinner] = useState(null);
        const winners = [
          {
            year: 2024,
            name: "José Carpintero",
            group: "1ºC",
            level: "Level A",
            winningWord: "beautiful",
            trophy: "🥇",
            photo: "IMG/1A.webp"
          },
          {
            year: 2024,
            name: "Ángela García",
            group: "2ºA",
            level: "Level B",
            winningWord: "magnificent",
            trophy: "🥇",
            photo: "IMG/2B.jpg"
          },
          {
            year: 2024,
            name: "Sofío Contle",
            group: "3ºC",
            level: "Level C",
            winningWord: "exhilarating",
            trophy: "🥇",
            photo: "IMG/3C.webp"
          },
          {
            year: 2023,
            name: "Ashley Camacho",
            group: "1ºC",
            level: "Level A",
            winningWord: "wonderful",
            trophy: "🏆"
          },
          {
            year: 2023,
            name: "Aisha Hernandez",
            group: "2ºA",
            level: "Level B",
            winningWord: "extraordinary",
            trophy: "🏆"
          },
          {
            year: 2023,
            name: "David Gamaliel",
            group: "3ºA",
            level: "Level C",
            winningWord: "conscientious",
            trophy: "🏆"
          }
        ];

        return React.createElement('div', { className: 'min-h-screen p-8' },
          React.createElement('div', { className: 'max-w-6xl mx-auto animate-fadeIn' },
            React.createElement('div', { className: 'flex items-center justify-between mb-8' },
              React.createElement('button', {
                onClick: () => setCurrentScreen('home'),
                className: 'bg-black text-yellow-400 p-3 rounded-full hover:bg-yellow-600 transition-all duration-300 shadow-lg border border-white/10'
              }, React.createElement(ArrowLeft, { className: 'w-6 h-6' })),
              React.createElement('div', { className: 'bg-black/60 text-yellow-400 py-4 px-8 rounded-xl font-bold text-5xl shadow-lg border border-white/10' },
                'Temple de la Renommée'
              ),
              React.createElement('div', { className: 'w-12' })
            ),
            
            React.createElement('div', { className: 'text-center mb-8' },
              React.createElement('div', { className: 'text-6xl mb-4' }, '🏆'),
              React.createElement('p', { className: 'text-3xl text-white font-semibold' },
                "Célébrons nos Champions d'Orthographe"
              )
            ),

            React.createElement('div', { className: 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6' },
              winners.map((winner, index) =>
                React.createElement('div', { 
                  key: index, 
                  className: `bg-black bg-opacity-40 backdrop-blur-xl rounded-2xl p-6 shadow-2xl border border-white border-opacity-15 transform hover:scale-105 transition-all duration-300 cursor-pointer ${
                    winner.year === 2024 ? 'ring-2 ring-yellow-400/30' : ''
                  }`,
                  onClick: () => setSelectedWinner(winner)
                },
                  React.createElement('div', { className: 'text-center' },
                    // Winner photo
                    winner.photo && React.createElement('div', { className: 'mb-4' },
                      React.createElement('img', {
                        src: winner.photo,
                        alt: `${winner.name} - Gagnant ${winner.year}`,
                        className: 'w-32 h-32 rounded-full mx-auto object-cover border-4 border-amber-500 shadow-lg'
                      })
                    ),
                    // Trophy & Year
                    React.createElement('div', { className: 'flex items-center justify-center gap-3 mb-3' },
                      React.createElement('div', { className: 'text-4xl' }, winner.trophy),
                      React.createElement('div', { className: 'bg-black text-yellow-400 rounded-full px-3 py-1 text-sm font-bold border border-white/10' },
                        winner.year
                      )
                    ),
                    React.createElement('h3', { className: 'text-xl font-bold text-yellow-400 mb-2' },
                      winner.name
                    ),
                    React.createElement('p', { className: 'text-gray-300 font-semibold mb-2' },
                      winner.group
                    ),
                    React.createElement('div', { className: 'bg-yellow-400/20 text-yellow-400 border border-yellow-400/30 rounded-lg px-3 py-1 text-sm font-bold mb-3 inline-block' },
                      winner.level
                    ),
                    React.createElement('div', { className: 'border-t border-white/10 pt-3' },
                      React.createElement('p', { className: 'text-sm text-gray-400 mb-1' }, 'Mot Gagnant:'),
                      React.createElement('p', { className: 'text-lg font-bold text-white' },
                        `"${winner.winningWord}"`
                      )
                    )
                  )
                )
              )
            ),

            // Details Modal popup
            selectedWinner && React.createElement('div', { 
              className: 'fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4',
              onClick: () => setSelectedWinner(null)
            },
              React.createElement('div', { 
                className: 'bg-black bg-opacity-80 backdrop-blur-xl rounded-2xl p-4 sm:p-6 shadow-2xl border border-white border-opacity-15 max-w-sm sm:max-w-md md:max-w-lg w-full mx-auto relative max-h-[85vh] overflow-y-auto transform transition-all duration-500 ease-out',
                onClick: (e) => e.stopPropagation(),
                style: {
                  animation: 'modalGrow 0.5s ease-out'
                }
              },
                React.createElement('div', { className: 'text-center' },
                  React.createElement('button', {
                    onClick: () => setSelectedWinner(null),
                    className: 'absolute top-2 right-2 sm:top-3 sm:right-3 bg-red-600 text-white rounded-full w-6 h-6 sm:w-7 sm:h-7 flex items-center justify-center hover:bg-red-700 transition-all duration-300 text-xs sm:text-sm z-10 border border-white/10'
                  }, '✕'),
                  selectedWinner.photo && React.createElement('div', { className: 'mb-3 sm:mb-4' },
                    React.createElement('img', {
                      src: selectedWinner.photo,
                      alt: `${selectedWinner.name} - Gagnant ${selectedWinner.year}`,
                      className: 'w-20 h-20 sm:w-24 sm:h-24 md:w-32 md:h-32 rounded-full mx-auto object-cover border-3 border-amber-500 shadow-lg'
                    })
                  ),
                  React.createElement('div', { className: 'flex items-center justify-center gap-2 sm:gap-3 mb-3 sm:mb-4' },
                    React.createElement('div', { className: 'text-2xl sm:text-3xl md:text-4xl' }, selectedWinner.trophy),
                    React.createElement('div', { className: 'bg-black text-yellow-400 rounded-full px-2 py-1 sm:px-3 sm:py-1 text-sm sm:text-base md:text-lg font-bold border border-white/10' },
                      selectedWinner.year
                    )
                  ),
                  React.createElement('h2', { className: 'text-lg sm:text-xl md:text-2xl font-bold text-white mb-2 sm:mb-3' },
                    selectedWinner.name
                  ),
                  React.createElement('p', { className: 'text-sm sm:text-base md:text-lg text-gray-300 font-semibold mb-2 sm:mb-3' },
                    selectedWinner.group
                  ),
                  React.createElement('div', { className: 'bg-yellow-400/20 text-yellow-400 border border-yellow-400/30 rounded-lg px-2 py-1 sm:px-3 sm:py-1 text-xs sm:text-sm md:text-base font-bold mb-3 sm:mb-4 inline-block' },
                    selectedWinner.level
                  ),
                  React.createElement('div', { className: 'border-t border-white/10 pt-3 sm:pt-4' },
                    React.createElement('p', { className: 'text-xs sm:text-sm md:text-base text-gray-400 mb-1 sm:mb-2' }, 'Mot Gagnant:'),
                    React.createElement('p', { className: 'text-base sm:text-lg md:text-xl font-bold text-white' },
                      `"${selectedWinner.winningWord}"`
                    )
                  )
                )
              )
            ),

            React.createElement('div', { className: 'mt-12 bg-black bg-opacity-40 backdrop-blur-xl rounded-2xl p-8 shadow-2xl border border-white border-opacity-15' },
              React.createElement('h2', { className: 'text-2xl font-bold text-yellow-400 mb-6 text-center' },
                'Statistiques du Concours'
              ),
              React.createElement('div', { className: 'grid grid-cols-1 md:grid-cols-3 gap-6 text-center' },
                React.createElement('div', { className: 'bg-gradient-to-br from-black to-gray-800 rounded-xl p-4 border border-white/10 shadow-lg' },
                  React.createElement('div', { className: 'text-3xl font-bold text-yellow-400' }, '150+'),
                  React.createElement('p', { className: 'text-white font-semibold' }, 'Participants au total')
                ),
                React.createElement('div', { className: 'bg-gradient-to-br from-red-600/20 to-red-700/20 rounded-xl p-4 border border-red-500/30 shadow-lg' },
                  React.createElement('div', { className: 'text-3xl font-bold text-red-500' }, '25'),
                  React.createElement('p', { className: 'text-white font-semibold' }, 'Écoles participantes')
                ),
                React.createElement('div', { className: 'bg-gradient-to-br from-yellow-400/10 to-yellow-500/10 rounded-xl p-4 border border-yellow-400/20 shadow-lg' },
                  React.createElement('div', { className: 'text-3xl font-bold text-yellow-400' }, '500+'),
                  React.createElement('p', { className: 'text-white font-semibold' }, 'Mots Épelés')
                )
              )
            )
          )
        );
      };\n\n      """

content = content_for_winners[:start_win] + winners_code + content_for_winners[end_win:]

# ----------------- REEMPLAZAR WORDLIST SCREEN -----------------
content_for_wl = content
start_wl = content_for_wl.find("const WordListScreen = () => {")
end_wl = content_for_wl.find("const NavigationBar = () => {")

if start_wl == -1 or end_wl == -1:
    print("Error: No se pudo encontrar WordListScreen o NavigationBar!")
    exit(1)

wordlist_code = """const WordListScreen = () => {
        const [searchTerm, setSearchTerm] = useState('');
        
        const levelName = levels[selectedLevel]?.name || 'Liste de mots';
        const words = levels[selectedLevel]?.words || [];
        
        const sortedWords = React.useMemo(() => {
          return [...words].sort((a, b) => a.word.localeCompare(b.word, 'fr', { sensitivity: 'base' }));
        }, [words]);
        
        const filteredWords = sortedWords.filter(item => 
          item.word.toLowerCase().includes(searchTerm.toLowerCase())
        );

        const handleDownload = () => {
          const headers = ['Mot', 'Prononciation', 'Définition', 'Exemple de phrase'];
          const csvRows = [];
          csvRows.push(headers.join(','));
          
          sortedWords.forEach(item => {
            const defRaw = item.definition || generateDefinition(item.word, levels[selectedLevel]?.name);
            const exRaw = item.example || generateExample(item.word, levels[selectedLevel]?.name);
            const def = defRaw.replace(/"/g, '""');
            const ex = exRaw.replace(/"/g, '""');
            const row = [
              `"${item.word}"`,
              `"${item.phonetic || ''}"`,
              `"${def}"`,
              `"${ex}"`
            ];
            csvRows.push(row.join(','));
          });
          
          const csvContent = "\\uFEFF" + csvRows.join("\\n");
          const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
          const url = URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.setAttribute("href", url);
          link.setAttribute("download", `Spelling_Bee_${levelName.replace(/\\s+/g, '_')}_Mots.csv`);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        };

        return React.createElement('div', { className: 'min-h-screen p-4 sm:p-8' },
          React.createElement('div', { className: 'max-w-5xl mx-auto animate-fadeIn' },
            React.createElement('div', { className: 'flex flex-col sm:flex-row items-center justify-between mb-6 sm:mb-8 gap-4' },
              React.createElement('div', { className: 'flex items-center gap-4 w-full sm:w-auto' },
                React.createElement('button', {
                  onClick: () => setCurrentScreen('menu'),
                  className: 'bg-black text-yellow-400 p-2 sm:p-3 rounded-full hover:bg-yellow-600 hover:text-black transition-all duration-300 shadow-lg transform hover:scale-110 border border-white/10'
                }, React.createElement(ArrowLeft, { className: 'w-5 h-5 sm:w-6 sm:h-6' })),
                React.createElement('h1', { className: 'text-2xl sm:text-4xl font-bold text-white tracking-wide drop-shadow-[0_2px_8px_rgba(0,0,0,0.8)]' }, `${levelName} - Liste de mots`)
              ),
              
              React.createElement('button', {
                onClick: handleDownload,
                className: 'w-full sm:w-auto bg-black text-yellow-400 hover:bg-yellow-600 hover:text-black font-bold py-3 px-6 rounded-xl shadow-lg transition-all duration-300 transform hover:scale-105 flex items-center justify-center gap-2 border border-white/10'
              }, 
                React.createElement('span', { className: 'text-xl' }, '📥'),
                'Télécharger la liste (CSV)'
              )
            ),

            React.createElement('div', { className: 'bg-black bg-opacity-40 backdrop-blur-xl rounded-2xl p-4 sm:p-8 shadow-2xl border border-white border-opacity-15' },
              React.createElement('div', { className: 'flex flex-col sm:flex-row items-center justify-between mb-6 gap-4 border-b border-white/10 pb-6' },
                React.createElement('div', { className: 'relative w-full sm:w-80' },
                  React.createElement('input', {
                    type: 'text',
                    placeholder: '🔍 Rechercher des mots...',
                    value: searchTerm,
                    onChange: (e) => setSearchTerm(e.target.value),
                    className: 'w-full px-4 py-3 bg-black bg-opacity-50 text-white border border-white border-opacity-20 rounded-xl focus:outline-none focus:ring-4 focus:ring-yellow-400 font-semibold shadow-md placeholder-gray-500 transition-all'
                  })
                ),
                React.createElement('div', { className: 'text-white font-extrabold text-base bg-white bg-opacity-10 border border-white border-opacity-20 px-4 py-2 rounded-xl shadow-lg' },
                  `Affichage de ${filteredWords.length} sur ${words.length} mots`
                )
              ),

              React.createElement('div', { className: 'overflow-x-auto max-h-[500px] border border-white border-opacity-15 rounded-2xl shadow-2xl bg-black bg-opacity-20' },
                React.createElement('table', { className: 'min-w-full divide-y divide-white/10 text-left' },
                  React.createElement('thead', { className: 'bg-black/85 text-yellow-400 sticky top-0 z-10' },
                    React.createElement('tr', null,
                      React.createElement('th', { className: 'px-6 py-4 font-extrabold text-sm sm:text-base border-r border-white/10' }, 'Mot'),
                      React.createElement('th', { className: 'px-6 py-4 font-extrabold text-sm sm:text-base border-r border-white/10' }, 'Prononciation'),
                      React.createElement('th', { className: 'px-6 py-4 font-extrabold text-sm sm:text-base border-r border-white/10' }, 'Définition'),
                      React.createElement('th', { className: 'px-6 py-4 font-extrabold text-sm sm:text-base' }, 'Exemple de phrase')
                    )
                  ),
                  React.createElement('tbody', { className: 'divide-y divide-white/10 bg-black/10 font-semibold text-gray-200' },
                    filteredWords.length === 0 
                      ? React.createElement('tr', null,
                          React.createElement('td', { colSpan: 4, className: 'px-6 py-12 text-center text-gray-400 font-bold text-lg' }, 'Aucun mot trouvé correspondant à votre recherche.')
                        )
                      : filteredWords.map((item, idx) => {
                          const definition = item.definition || generateDefinition(item.word, levels[selectedLevel]?.name);
                          const example = item.example || generateExample(item.word, levels[selectedLevel]?.name);
                          return React.createElement('tr', { 
                            key: idx,
                            className: 'hover:bg-white/5 transition-colors duration-150'
                          },
                            React.createElement('td', { className: 'px-6 py-4 text-white font-black text-base whitespace-nowrap border-r border-white/10' }, item.word),
                            React.createElement('td', { className: 'px-6 py-4 text-yellow-400 font-mono text-sm whitespace-nowrap border-r border-white/10 bg-black/20' }, item.phonetic || '-'),
                            React.createElement('td', { className: 'px-6 py-4 text-gray-300 text-sm max-w-xs border-r border-white/10' }, definition),
                            React.createElement('td', { className: 'px-6 py-4 text-gray-300 text-sm italic max-w-sm' }, example)
                          );
                        })
                  )
                )
              )
            )
          )
        );
      };\n\n      """

content = content_for_wl[:start_wl] + wordlist_code + content_for_wl[end_wl:]

# ----------------- REEMPLAZAR LOGO EN NAVIGATION BAR -----------------
content_for_nav = content
old_logo_markup = """              React.createElement('div', { className: 'text-yellow-400 font-bold text-xl' },
                '🐝 Spelling Bee'
              ),"""

new_logo_markup = """              React.createElement('div', { className: 'flex items-center gap-3 cursor-pointer', onClick: () => { setGameMode(null); setCurrentScreen('home'); } },
                React.createElement('div', { className: 'relative w-9 h-9 flex items-center justify-center' },
                  React.createElement('div', {
                    className: 'absolute inset-0 bg-black border border-yellow-400 border-opacity-70 flex items-center justify-center',
                    style: {
                      clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                      WebkitClipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)'
                    }
                  },
                    React.createElement('img', {
                      src: 'IMG/Abeja.png',
                      alt: 'Logo Bee',
                      className: 'w-8 h-8 object-contain filter drop-shadow-[0_2px_8px_rgba(253,224,71,0.45)]'
                    })
                  )
                ),
                React.createElement('span', { className: 'font-black text-sm sm:text-base tracking-wider text-white' },
                  'SPELLING ',
                  React.createElement('span', { className: 'text-yellow-400' }, 'BEE')
                )
              ),"""

if old_logo_markup not in content_for_nav:
    print("Warning: could not find old logo markup in NavigationBar!")
else:
    content = content_for_nav.replace(old_logo_markup, new_logo_markup)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("French fix completed successfully!")
