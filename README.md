# Classic Confections Packaging MCP

MCP server for generating vintage candy packaging aesthetics spanning 1890s-1970s. Uses three-layer architecture for cost-efficient prompt enhancement: Claude intent analysis → deterministic taxonomy mapping → creative synthesis.

## Cost Optimization

- **~60-80% token savings** vs pure LLM approach
- Layer 1: Intent analysis (1 Claude call, ~500 tokens)
- Layer 2: Deterministic mapping (0 tokens, pure Python)
- Layer 3: Creative synthesis (1 Claude call, ~1000 tokens)
- **Total: ~1500 tokens vs 4000+ for pure LLM**

## Architecture Pattern

```
User Prompt
    ↓
[Claude] Intent Analysis → JSON
    ↓
[MCP] Deterministic Mapping → Parameters
    ↓
[Claude] Creative Synthesis → Enhanced Prompt
```

Separates creative interpretation (Claude) from taxonomy expertise (MCP).

## Installation

```bash
cd classic-confections-mcp
pip install -e .
```

## Usage

### Three-Step Workflow (Recommended)

```python
# Step 1: Analyze intent (Claude)
result = analyze_packaging_intent(
    "1920s luxury chocolate bar wrapper with gold accents"
)
# Returns: {"era": "art_deco_1920s", "candy_type": "chocolate_bar", ...}

# Step 2: Map parameters deterministically (MCP - zero tokens)
params = map_packaging_parameters(json.dumps(result))
# Returns: Complete visual parameter specification

# Step 3: Synthesize final prompt (Claude)
final = synthesize_packaging_prompt(
    "1920s luxury chocolate bar wrapper with gold accents",
    json.dumps(params)
)
# Returns: Detailed enhanced prompt for image generation
```

### Quick Workflow Guide

```python
# Get workflow instructions
guide = enhance_packaging_prompt(
    "Art Nouveau candy tin with flowing floral patterns"
)
```

## Era Coverage

### Victorian (1890s)
- Ornate serif typography, decorative capitals
- Botanical borders, cherubs, ribbon banners
- Deep jewel tones, gold accents
- Centered symmetrical composition

### Art Nouveau (1900s)
- Flowing organic letterforms, whiplash curves
- Stylized flora, maiden figures, peacock motifs
- Muted pastels, nature greens, copper/bronze
- Organic asymmetrical layout

### Art Deco (1920s)
- Geometric sans serif, streamlined forms
- Sunburst patterns, zigzag borders, chevrons
- Black/gold, chrome silver, bold contrast
- Vertical emphasis, geometric precision

### Depression Era (1930s)
- Condensed gothic, economical lettering
- Simple borders, value messaging, wholesome scenes
- Two-color printing, kraft brown, red/blue basics
- Efficient readable design

### Wartime (1940s)
- Bold sans serif, patriotic block letters
- Stars and stripes, victory themes, ration messaging
- Red/white/blue, kraft paper, utilitarian palette
- Direct utilitarian communication

### Mid-Century (1950s)
- Atomic age script, Googie lettering
- Boomerang shapes, starbursts, kidney shapes
- Turquoise/pink, avocado/orange, chrome accents
- Dynamic diagonal compositions

### Psychedelic (1960s)
- Groovy bubble letters, op-art distortion
- Swirls, paisley, flower power, mandala forms
- Neon saturation, purple/orange, acid brights
- All-over pattern coverage

### Retro (1970s)
- Rounded friendly type, fat face serif
- Rainbow stripes, smiley faces, disco elements
- Earth tones, harvest gold, burnt orange/brown
- Centered bold simple design

## Package Format Types

### Twist Wrap
- **Structure**: Cylindrical with twisted ends
- **Materials**: Wax paper, foil, cellophane
- **Typical candy**: Hard candies, taffy, caramels
- **Display**: Bulk jars, counter rolls

### Bar Wrapper
- **Structure**: Flat rectangular fold, foil edges visible
- **Materials**: Foil inner, paper outer, glassine
- **Typical candy**: Chocolate bars, candy bars
- **Display**: Counter boxes, standing racks

### Box and Sleeve
- **Structure**: Inner tray in decorative outer sleeve
- **Materials**: Coated cardboard, embossed paper, die-cut windows
- **Typical candy**: Assorted chocolates, premium confections
- **Display**: Shelf facing, gift presentation

### Tin Container
- **Structure**: Hinged or slip-lid metal with all-over decoration
- **Materials**: Lithographed tin, embossed metal
- **Typical candy**: Mints, hard candies, toffees
- **Display**: Counter display, gift tin

### Cellophane Bag
- **Structure**: Clear bag with printed header card
- **Materials**: Clear cellophane, printed card top
- **Typical candy**: Gummies, jellies, wrapped assortments
- **Display**: Pegboard hanging, counter bins

### Counter Jar
- **Structure**: Glass jar with decorative lid and label
- **Materials**: Clear glass, metal lid, paper label
- **Typical candy**: Penny candies, bulk confections
- **Display**: Drugstore/candy shop counter

## Brand Personality Types

### Premium Luxury
- Gold foil accents, embossing, elegant script, French phrases
- Best eras: Art Nouveau, Art Deco
- Messaging: Superior quality, refined taste, special occasion

### Wholesome Family
- Hand-drawn children, farm scenes, home-made quality
- Best eras: Depression, Wartime, 1950s
- Messaging: Family tradition, pure ingredients, trusted recipe

### Novelty Fun
- Cartoon mascots, bright colors, kid appeal, playful illustration
- Best eras: 1950s, 1960s, 1970s
- Messaging: Fun excitement, flavor adventure, playful energy

### Traditional Heritage
- Established date, family recipe, old-world imagery, heritage seals
- Best eras: Victorian, Art Nouveau, Depression
- Messaging: Time-tested quality, authentic recipe, generations

### Modern Progressive
- Clean lines, contemporary style, innovative messaging
- Best eras: 1950s, 1960s, 1970s
- Messaging: New and improved, forward-thinking, contemporary

## Material Vocabulary

### Foil
- Reflective metallic, embossed texture, crisp angular folds
- Peak era: 1920s-1960s
- Colors: Gold, silver, colored foil, bronze

### Wax Paper
- Translucent matte, soft organic folds, printed flat colors
- Peak era: 1900s-1950s
- Colors: White, cream, pastels, two-color print

### Cellophane
- Glossy transparent, crinkled texture, tape sealed
- Peak era: 1930s-1970s
- Colors: Clear, tinted, printed overlay

### Lithographed Tin
- Rich printed colors on metal, embossed details, aged patina
- Peak era: 1890s-1930s
- Full color illustration, gold trim

### Coated Cardboard
- Matte/glossy coating, die-cut windows, fold lines visible
- Peak era: 1940s-1970s
- Vibrant offset printing, spot colors

### Embossed Paper
- Raised decorative patterns, textured surface, dimensional details
- Peak era: 1890s-1920s
- Metallic foil stamping, rich solid colors

## Example Prompts

### Art Deco Chocolate Bar
```
Input: "1920s luxury chocolate bar with geometric patterns"

Output: "A 1920s Art Deco chocolate bar wrapper with geometric 
sophistication. Gold foil inner wrapper visible at crisp folded edges, 
outer sleeve in rich black paper with embossed gold sunburst pattern 
radiating from centered brand name in elegant streamlined serif with 
inline metallic detail. Stepped architectural borders frame the 
composition. French phrase 'Chocolat Superieur' in delicate script 
below. Sharp angular folds catch light, showing metallic shimmer. 
Premium department store counter display lighting, slight shadow 
showing dimensional embossing."
```

### Victorian Tin Container
```
Input: "Victorian peppermint tin with botanical decoration"

Output: "Victorian 1890s peppermint tin with ornate botanical elegance. 
Lithographed metal container with embossed raised details showing 
intricate hand-drawn floral borders, delicate vines and roses in deep 
burgundy and forest green with gold accent trim. Ornate serif 
typography with decorative capitals, centered symmetrical composition. 
'Est. 1847' heritage seal. Aged metal patina showing gentle wear at 
edges. Hinged lid with embossed flower pattern. Old-world pharmacy 
counter context, warm gas lamp lighting, traditional dignified 
presentation."
```

### 1950s Novelty Candy
```
Input: "Atomic age bubble gum with space theme"

Output: "1950s atomic age bubble gum wrapper with kinetic space-age 
energy. Dynamic swooping Googie script with starburst accents, cartoon 
rocket mascot with big eyes and friendly smile. Boomerang shapes and 
kidney-form decorative elements in turquoise, hot pink, and chrome 
silver. Bold diagonal composition suggesting forward motion. Wax paper 
wrapper with vibrant two-color offset printing. 'Blast-Off Flavor!' in 
atomic script. Drugstore candy rack display, fluorescent lighting, 
optimistic suburban consumer culture aesthetic. Clean modern appeal to 
space-obsessed kids."
```

### 1960s Psychedelic
```
Input: "Groovy psychedelic candy with flower power design"

Output: "1960s psychedelic candy wrapper with vibrant counterculture 
energy. Bubble letters in flowing groovy forms, distorted op-art 
effects creating visual vibration. All-over pattern of stylized 
daisies, swirling paisley, and concentric rainbow circles. Neon 
saturated colors: electric purple, hot orange, acid green, shocking 
pink. Youth culture excitement, flower power messaging. Cellophane bag 
with printed header card showing mandala-like pattern. 'Far Out Flavor 
Trip!' in bubble script. Head shop or teen boutique context, black 
light poster aesthetic, rebellious playful spirit."
```

## Exploration Tools

### List Available Eras
```python
list_available_eras()
# Returns all eras with key characteristics
```

### List Package Formats
```python
list_package_formats()
# Returns all format types with typical candies
```

### List Brand Personalities
```python
list_brand_personalities()
# Returns brand tones and their cues
```

### Get Recommended Combinations
```python
get_era_combinations()
# Returns curated era + brand tone pairings
```

## Design Philosophy

**Focus: Packaging over candy itself**
- Packaging has richer visual vocabulary (typography, illustration, materials)
- Stronger era specificity and cultural markers
- More storytelling density (brand identity, claims, decorative elements)
- Better preserved in historical archives

**Vintage sweet spot: 1890s-1970s**
- Golden age of candy branding (pre-corporate consolidation)
- Peak decorative packaging (pre-minimalism cost-cutting)
- Strong nostalgic resonance
- Clear visual grammar per era

**Three-layer architecture benefits:**
1. Intent analysis captures creative nuance (Claude strength)
2. Deterministic mapping ensures taxonomic accuracy (MCP strength)
3. Synthesis combines parameters into cohesive atmosphere (Claude strength)

## Cross-Pollination with Other MCPs

### Magazine Photography MCP
- Combine for vintage candy advertising shoots
- Product photography lighting from magazine era
- Editorial styling and composition

### Cereal Box Style MCP
- Related vintage packaging design language
- Similar typography and illustration approaches
- Breakfast table nostalgia overlap

### Game Show Aesthetics MCP
- Prize display presentation contexts
- 1970s game show candy prizes
- Retail-oriented lighting and staging

## Technical Notes

- Uses FastMCP framework
- No external API calls for Layer 2 (deterministic)
- JSON-based parameter passing between layers
- Comprehensive taxonomy coverage (8 eras, 6 formats, 5 brand tones)
- Material-focused visual vocabulary
- Era-appropriate typography systems

## Future Enhancements

- Regional candy traditions (British toffee, Japanese wagashi influence)
- Candy store environment generation
- Multi-package display compositions
- Animation/motion for unwrapping sequences
- Chemistry angle: sugar crystallization, tempering patterns
- Holiday seasonal variations (Christmas, Halloween, Valentine's)

## License

MIT

## Author

Dal Marsters - Lushy AI Workflows
