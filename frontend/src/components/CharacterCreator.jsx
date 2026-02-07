import React, { useState } from 'react';

const App = () => {
  const [gameState, setGameState] = useState('landing'); // landing, creation, playing
  const [character, setCharacter] = useState({ name: '', class: 'Warrior', str: 10, dex: 10 });
  const [logs, setLogs] = useState([]);

  const startAdventure = () => setGameState('creation');
  
  const finalizeChar = () => {
    setLogs([{ type: 'dm', text: `Welcome, ${character.name} the ${character.class}. Your journey begins...` }]);
    setGameState('playing');
  };

  const exportStory = () => {
    const element = document.createElement("a");
    const file = new Blob([logs.map(l => `${l.type}: ${l.text}`).join('\n')], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = "adventure_transcript.txt";
    element.click();
  };

  if (gameState === 'landing') return (
    <div className="flex flex-col items-center justify-center h-screen bg-slate-900 text-white">
      <h1 className="text-5xl font-bold mb-8">AI Dungeon Master</h1>
      <button onClick={startAdventure} className="px-6 py-3 bg-red-600 hover:bg-red-700 rounded-lg">Start Adventure</button>
    </div>
  );

  return (
    <div className="flex h-screen bg-slate-800 text-slate-100 p-4 gap-4">
      {/* Sidebar: Stats & Dice */}
      <div className="w-1/4 bg-slate-900 p-4 rounded-xl border border-slate-700">
        <h2 className="text-xl font-bold border-b border-slate-700 pb-2">{character.name}</h2>
        <p className="text-sm text-slate-400 mb-4">{character.class}</p>
        <div className="space-y-2 mb-8">
          <div>HP: ❤️ 20/20</div>
          <div>STR: {character.str} | DEX: {character.dex}</div>
        </div>
        <div className="bg-slate-800 p-3 rounded text-center">
          <p className="text-xs uppercase text-slate-500">Last Dice Result</p>
          <div className="text-3xl font-mono font-bold text-yellow-400">18</div>
        </div>
        <button onClick={exportStory} className="mt-auto w-full py-2 bg-slate-700 hover:bg-slate-600 rounded mt-10">Export Story</button>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col bg-slate-900 rounded-xl border border-slate-700">
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {logs.map((log, i) => (
            <div key={i} className={`p-3 rounded-lg ${log.type === 'dm' ? 'bg-slate-800' : 'bg-blue-900 ml-12'}`}>
              <strong>{log.type === 'dm' ? '🐲 DM: ' : '👤 You: '}</strong>{log.text}
            </div>
          ))}
        </div>
        <div className="p-4 border-t border-slate-700">
          <input className="w-full bg-slate-800 p-3 rounded-lg outline-none" placeholder="What do you do?" />
        </div>
      </div>
    </div>
  );
};

export default App;