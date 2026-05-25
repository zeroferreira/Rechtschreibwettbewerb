# -*- coding: utf-8 -*-
import os

app_path = "/Users/zeroferreira/Documents/Material English/Spelling 2026/German/js/app.js"

# Read as bytes to avoid any decoding issues
with open(app_path, "rb") as f:
    content_bytes = f.read()

# Define the start and end anchors for the corruption as bytes
start_anchor = b"const Instru"
end_anchor = b"const NavigationBar"

start_idx = content_bytes.find(start_anchor)
end_idx = content_bytes.find(end_anchor)

if start_idx == -1:
    print("Error: Could not find start anchor!")
    exit(1)

if end_idx == -1:
    print("Error: Could not find end anchor!")
    exit(1)

print(f"Found start anchor at {start_idx} and end anchor at {end_idx}")

# Define the replacement code block (which is the correct, fixed InstructionsScreen)
replacement_code = """const InstructionsScreen = () => {
      const toggleSection = (sect) => {
        setExpandedSection(expandedSection === sect ? null : sect);
      };

      return React.createElement('div', { className: 'min-h-screen p-4 sm:p-8 flex items-center justify-center' },
        React.createElement('div', { className: 'max-w-5xl w-full bg-black bg-opacity-40 backdrop-blur-xl rounded-3xl p-6 sm:p-10 shadow-2xl border border-white border-opacity-15 relative min-h-[500px] flex flex-col md:flex-row gap-8 animate-fadeIn' },
          
          React.createElement('button', {
            onClick: () => setCurrentScreen('home'),
            className: 'absolute top-4 left-4 bg-black text-yellow-400 p-2 sm:p-3 rounded-full hover:bg-yellow-600 hover:text-black transition-all duration-300 shadow-lg transform hover:scale-110 z-10 border border-white/10'
          }, React.createElement(ArrowLeft, { className: 'w-5 h-5 sm:w-6 sm:h-6' })),

          // Left Panel: Hexagonal badges selector
          React.createElement('div', { className: 'w-full md:w-48 flex flex-row md:flex-col justify-center items-center gap-4 mt-8 md:mt-0 flex-wrap' },
            
            // Hexagon 1: Objective
            React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
              React.createElement('button', {
                onClick: () => toggleSection('objective'),
                className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                  expandedSection === 'objective' ? 'bg-green-500 text-black border-green-600' : ''
                }`,
                style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
              }, 
                React.createElement('div', { className: 'text-2xl mb-1' }, '🎯'),
                React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Ziel')
              )
            ),

            // Hexagon 2: Levels
            React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
              React.createElement('button', {
                onClick: () => toggleSection('levels'),
                className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                  expandedSection === 'levels' ? 'bg-green-500 text-black border-green-600' : ''
                }`,
                style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
              }, 
                React.createElement('div', { className: 'text-2xl mb-1' }, '📚'),
                React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Stufen')
              )
            ),

            // Hexagon 3: Modes
            React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
              React.createElement('button', {
                onClick: () => toggleSection('modes'),
                className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                  expandedSection === 'modes' ? 'bg-green-500 text-black border-green-600' : ''
                }`,
                style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
              }, 
                React.createElement('div', { className: 'text-2xl mb-1' }, '🎮'),
                React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Modi')
              )
            ),

            // Hexagon 4: How to Play
            React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
              React.createElement('button', {
                onClick: () => toggleSection('howToPlay'),
                className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                  expandedSection === 'howToPlay' ? 'bg-green-500 text-black border-green-600' : ''
                }`,
                style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
              }, 
                React.createElement('div', { className: 'text-2xl mb-1' }, '🎲'),
                React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Ablauf')
              )
            ),

            // Hexagon 5: Features
            React.createElement('div', { className: 'relative w-20 h-20 sm:w-24 sm:h-24' },
              React.createElement('button', {
                onClick: () => toggleSection('features'),
                className: `absolute inset-0 bg-yellow-400 hover:bg-yellow-300 text-black font-extrabold flex flex-col items-center justify-center shadow-lg transition-all duration-300 border border-yellow-400/20 ${
                  expandedSection === 'features' ? 'bg-green-500 text-black border-green-600' : ''
                }`,
                style: { clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)' }
              }, 
                React.createElement('div', { className: 'text-2xl mb-1' }, '🔧'),
                React.createElement('div', { className: 'text-[10px] font-bold uppercase' }, 'Features')
              )
            )

          ),

          // Right Panel: Expanded detailed content
          React.createElement('div', { className: 'flex-1 mt-6 md:mt-8' },
            !expandedSection && React.createElement('div', { className: 'flex items-center justify-center h-full text-center' },
              React.createElement('div', null,
                React.createElement('div', { className: 'text-6xl mb-4 animate-bounce' }, '🐝'),
                React.createElement('h3', { className: 'text-2xl font-black text-white mb-2' }, 'Wähle einen Bereich'),
                React.createElement('p', { className: 'text-gray-300 font-semibold' }, 'Klicke auf ein Sechseck links, um Details anzuzeigen.')
              )
            ),

            expandedSection === 'objective' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
              React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                React.createElement('span', null, '🎯'), 'Spielziel'
              ),
              React.createElement('p', { className: 'text-gray-200 leading-relaxed font-semibold text-base sm:text-lg' },
                'Das Ziel dieses Spiels ist es, deine Rechtschreibkompetenz im Deutschen spielerisch zu stärken. Durch Zuhören der Aussprache und das Eintippen der korrekten Schreibweise verbesserst du dein Sprachgefühl und Wortverständnis.'
              )
            ),

            expandedSection === 'levels' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
              React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                React.createElement('span', null, '📚'), 'Verfügbare Stufen'
              ),
              React.createElement('ul', { className: 'space-y-4 font-semibold text-gray-200 text-sm sm:text-base' },
                React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                  React.createElement('span', { className: 'w-4 h-4 bg-emerald-500 rounded-full mr-3 mt-1' }),
                  React.createElement('div', null,
                    React.createElement('strong', { className: 'text-yellow-400' }, 'Stufe A: '), 'A1, A2, KET - Grundwörter'
                  )
                ),
                React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                  React.createElement('span', { className: 'w-4 h-4 bg-blue-500 rounded-full mr-3 mt-1' }),
                  React.createElement('div', null,
                    React.createElement('strong', { className: 'text-yellow-400' }, 'Stufe B: '), 'B1, B1+, PET - Mittlere Wörter'
                  )
                ),
                React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                  React.createElement('span', { className: 'w-4 h-4 bg-purple-500 rounded-full mr-3 mt-1' }),
                  React.createElement('div', null,
                    React.createElement('strong', { className: 'text-yellow-400' }, 'Stufe C: '), 'B2, C1, C2, FC, CAE - Fortgeschrittene Wörter'
                  )
                )
              )
            ),

            expandedSection === 'modes' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
              React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                React.createElement('span', null, '🎮'), 'Spielmodi'
              ),
              React.createElement('ul', { className: 'space-y-4 font-semibold text-gray-200 text-sm sm:text-base' },
                React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                  React.createElement('span', { className: 'w-4 h-4 bg-emerald-500 rounded-full mr-3 mt-1' }),
                  React.createElement('div', null,
                    React.createElement('strong', { className: 'text-yellow-400' }, 'Wettbewerb: '), 'Spiele gegen die Zeit (30 Sek.) mit maximal 3 Fehlern.'
                  )
                ),
                React.createElement('li', { className: 'flex items-start p-4 bg-black/40 rounded-xl shadow-md border border-white/10' },
                  React.createElement('span', { className: 'w-4 h-4 bg-blue-500 rounded-full mr-3 mt-1' }),
                  React.createElement('div', null,
                    React.createElement('strong', { className: 'text-yellow-400' }, 'Training: '), 'Übe frei und ohne Zeitlimit, schaue dir Definitionen und Sätze an.'
                  )
                )
              )
            ),

            expandedSection === 'howToPlay' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn overflow-y-auto max-h-[380px]' },
              React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                React.createElement('span', null, '🎲'), 'Spielablauf'
              ),
              React.createElement('ol', { className: 'space-y-3 font-semibold text-gray-200 text-sm sm:text-base list-decimal pl-4' },
                React.createElement('li', null, 'Wähle dein Schwierigkeitslevel (A, B oder C).'),
                React.createElement('li', null, 'Wähle zwischen Wettbewerb oder Training.'),
                React.createElement('li', null, 'Zuhöre dem Wort, indem du auf die Aussprache-Schaltfläche klickst.'),
                React.createElement('li', null, 'Gib die korrekte Schreibweise im Eingabefeld ein (oder buchstabiere per Mikrofon).'),
                React.createElement('li', null, 'Nutze die Hilfen wie Definitionen oder Beispielsätze im Trainingsmodus.'),
                React.createElement('li', null, 'Tippe auf Bestätigen, um deine Antwort auszuwerten.')
              )
            ),

            expandedSection === 'features' && React.createElement('div', { className: 'p-6 bg-black bg-opacity-30 rounded-2xl border border-white border-opacity-10 h-full animate-fadeIn' },
              React.createElement('h3', { className: 'text-2xl sm:text-3xl font-black text-yellow-400 mb-4 flex items-center gap-3' }, 
                React.createElement('span', null, '🔧'), 'Technische Features'
              ),
              React.createElement('ul', { className: 'space-y-2.5 font-semibold text-gray-200 text-sm sm:text-base' },
                React.createElement('li', null, '• Native Sprachsynthese mit Unterstützung für deutsche Dialekte.'),
                React.createElement('li', null, '• Sprach-zu-Text-Erkennung mit Unterstützung für Diktieren.'),
                React.createElement('li', null, '• Dynamischer Tages-/Nachtmodus mit kosmetischen Anpassungen.'),
                React.createElement('li', null, '• CSV-Export zum Herunterladen vollständiger Vokabellisten.'),
                React.createElement('li', null, '• Premium Glassmorphismus-Design mit flexiblen Animationen.')
              )
            )
          )

        )
      );
    };

    """.encode('utf-8')

fixed_content_bytes = content_bytes[:start_idx] + replacement_code + content_bytes[end_idx:]

with open(app_path, "wb") as f:
    f.write(fixed_content_bytes)

print("Fix completed successfully!")
