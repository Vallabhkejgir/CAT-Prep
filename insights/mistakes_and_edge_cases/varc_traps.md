# VARC Option-Elimination Traps, Scope Creeps & TITA Pitfalls Manual

In CAT VARC, the difference between an 85%iler and a 99.9%iler is **not reading speed or vocabulary size**—it is the ability to spot how a test-maker poisons a 90%-accurate option with a 2-word distortion. Use this manual to diagnose every VARC mistake during mock analysis.

---

## 1. The Complete RC Distractor Engineering Catalogue

### 1.1 Modifier & Quantifier Distortions
- **Soft-to-Hard Escalation**:
  - *Passage*: *"Urbanization **can** erode informal kinship networks."*
  - *Trap Option*: *"Urbanization **inevitably destroys** informal kinship networks."*
- **Frequency Inflation**:
  - *Passage*: *"Several 19th-century novelists experimented with serialized cliffhangers."* (`Some`)
  - *Trap Option*: *"Serialized cliffhangers were the dominant mode of 19th-century fiction."* (`Most / Dominant`)
- **Superlative Fabrication**:
  - *Passage*: *"High housing costs are a major barrier to labor mobility."* (`A major barrier`)
  - *Trap Option*: *"High housing costs are the primary barrier to labor mobility."* (`The #1 barrier`)

### 1.2 Structural & Relational Distortions
- **Fake Comparison (Apples & Oranges)**:
  - Whenever an option contains `more than`, `less than`, `better than`, `easier than`, `as much as`, or `unlike`, immediately verify whether the passage **explicitly compared those two things on that exact dimension**. If the passage merely mentioned both without ranking them, **eliminate immediately**.
- **Reverse Causality & Third-Factor Confusion**:
  - Passage says $A \to B$; option says $B \to A$.
  - Passage says $C$ causes both $A$ and $B$; option says $A$ causes $B$.
- **Necessary vs. Sufficient Condition Swap**:
  - *Passage*: *"Without independent courts, property rights cannot be secure."* (`Independent courts` are **necessary** for secure property rights.)
  - *Trap Option*: *"Establishing independent courts guarantees secure property rights."* (Treats them as **sufficient**!)

### 1.3 Scope, Voice & Question-Stem Distortions
- **Descriptive (`Is`) $\to$ Normative (`Should`) Creep**:
  - Academic passages often analyze a phenomenon without advocating a law or ban. Any option introducing `should, must, ought to, needs to` when the author stayed descriptive is wrong.
- **Voice Misattribution (The "Strawman / Old View" Trap)**:
  - Paragraph 1 summarizes what *critics of globalization* claim; Paragraph 2 gives the *author's rebuttal*. A classic trap option asks *"According to the author..."* and quotes Paragraph 1's critics verbatim.
- **Right Line, Wrong Question**:
  - Question asks: *"Which of the following explains WHY the experiment failed?"*
  - Trap Option quotes a true sentence from the passage stating *WHEN the experiment was conducted* or *WHAT its consequence was*.

---

## 2. Verbal Ability (VA) Pitfalls & Illusions

### 2.1 Para-Jumbles (TITA) Traps
1. **The False Chronology Trap**:
   - Students automatically put a sentence mentioning `1920` before a sentence mentioning `2020`.
   - **Watch Out**: Academic paragraphs frequently open with a **modern puzzle (`In 2020...`)** and then flash back (`The roots of this policy trace back to 1920...`)! Check grammatical connectors (`trace back to`, `had previously`) before blindly sorting by year.
2. **The Premature Pronoun Placement (`A-B` vs `B-A`)**:
   - Placing `They argue that...` *before* the sentence introducing `behavioral economists`.
3. **The Misplaced "However" Pivot**:
   - If two sentences are negative ($N_1, N_2$) and one is positive ($P_1$), the `However` pivot MUST sit at the exact transition $P_1 \to N_1$ (or $N_1 \to P_1$), never between two sentences of the same polarity!

### 2.2 Odd-One-Out (TITA) Traps
1. **The "Shared Keyword" Bait**:
   - All 5 sentences contain the phrase *"quantum computing"*. Four sentences form a tight cause-effect chain about **cryptographic security risks** (even using `it` or `this threat` in one sentence), while the 5th sentence talks about **cooling hardware temperatures in quantum computers**. Students wrongly eliminate the pronoun sentence instead of the off-angle cooling sentence!
2. **Skipping the 4-Sentence Jumble Verification**:
   - Never lock an Odd-One-Out answer until you can read the remaining 4 sentences in a specific order (`e.g., 3-1-5-2`) as a seamless paragraph.

### 2.3 Para-Summary & Sentence Placement (MCQ) Traps
1. **The Example-Heavy Summary Trap**:
   - In Para-Summary, an option that names the specific examples (*"like Kodak and Nokia"*) while missing the general principle (*"incumbent firms fail when they cannibalize R&D"*) is ALWAYS inferior to the option that states the general principle cleanly.
2. **Breaking a Mandatory Pair in 4-Slot Sentence Placement**:
   - Before testing where target sentence $S$ fits among `[1] [2] [3] [4]`, check which adjacent sentences in the base paragraph already lock together via `This / Such / They`. Cross out any slot `[k]` that sits inside an unbreakable pair!
