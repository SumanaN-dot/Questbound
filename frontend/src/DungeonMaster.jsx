import "./style.css";

export default function DungeonMaster() {
  return (
    <>
      {/* NAVBAR */}
      <header className="navbar">
        <div className="logo">AI Dungeon Master</div>

        <nav>
          <a href="#">About DM</a>
          <a href="#">Rules</a>
          <button className="ghost-btn">Log In</button>
          <button className="blood-btn">Sign Up</button>
        </nav>
      </header>

      {/* HERO */}
      <section className="hero">
        <h1>
          Your Personal <br />
          <span>AI Dungeon Master</span>
        </h1>

        <p>
          A sentient Dungeon Master that remembers your choices, twists fate, and
          punishes recklessness. Every decision matters. Death is permanent.
        </p>

        <div className="hero-buttons">
          <button className="blood-btn">Begin the Descent</button>
          <button
            className="ghost-btn"
            onClick={() =>
              window.open("https://www.youtube.com/", "_blank")
            }
          >
            Watch a Demo
          </button>
        </div>
      </section>

      {/* RULES */}
      <section className="rules">
        <h2>The Rules of the Dungeon</h2>

        <ul>
          <li>Your choices shape the world — there are no takebacks.</li>
          <li>Reckless actions may lead to permanent consequences.</li>
          <li>The Dungeon Master is impartial, but not merciful.</li>
          <li>Some encounters cannot be won — only survived.</li>
          <li>If you die, your story ends.</li>
        </ul>

        <ul>
          <li>20 sided dice! Your roll decides your fate.</li>
          <li>If you roll 1-10, you face a dire consequence.</li>
          <li>If you roll 11-19, you narrowly escape with your life.</li>
          <li>If you roll a 20, you achieve a heroic victory.</li>
          <li>Difficulty levels: Easy, Medium, Hard</li>
          <li>Character Options: Mage, Warrior, Rogue, Paladin</li>
        </ul>
      </section>
    </>
  );
}
