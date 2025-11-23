"""
Classic Confections Packaging MCP Server

Three-layer architecture for vintage candy packaging aesthetics (1890s-1970s):
1. Intent analysis (Claude) - extract era, tone, candy type
2. Deterministic mapping (MCP) - taxonomy to visual parameters
3. Creative synthesis (Claude) - final enhanced prompt

Cost optimization: ~60% savings vs pure LLM approach
"""

from fastmcp import FastMCP
import json

mcp = FastMCP("Classic Confections Packaging")

# ============================================================================
# LAYER 2: DETERMINISTIC TAXONOMIES
# ============================================================================

ERA_STYLES = {
    "victorian_1890s": {
        "typography": ["ornate_serif", "hand_lettered_script", "decorative_capitals"],
        "decoration": ["botanical_borders", "cherubs", "ribbon_banners", "floral_corners"],
        "colors": ["deep_jewel_tones", "gold_accents", "burgundy", "forest_green"],
        "composition": "centered_symmetrical",
        "atmosphere": "ornate Victorian elegance, highly decorated, intricate details"
    },
    "art_nouveau_1900s": {
        "typography": ["flowing_organic", "whiplash_curves", "nature_inspired_letters"],
        "decoration": ["stylized_flora", "maiden_figures", "peacock_motifs", "sinuous_vines"],
        "colors": ["muted_pastels", "nature_greens", "copper_bronze", "lilac_mauve"],
        "composition": "organic_asymmetrical",
        "atmosphere": "Art Nouveau flowing lines, organic forms, feminine elegance"
    },
    "art_deco_1920s": {
        "typography": ["geometric_sans", "streamlined_serif", "inline_patterns"],
        "decoration": ["sunburst_patterns", "zigzag_borders", "stepped_forms", "chevron_details"],
        "colors": ["black_gold", "chrome_silver", "bold_contrast", "deep_brown"],
        "composition": "vertical_emphasis_geometric",
        "atmosphere": "Art Deco sophistication, geometric precision, metallic glamour"
    },
    "depression_1930s": {
        "typography": ["condensed_gothic", "hand_brush_casual", "economical_lettering"],
        "decoration": ["simple_borders", "price_emphasis", "wholesome_scenes", "minimal_ornament"],
        "colors": ["economical_two_color", "red_blue_basics", "kraft_brown"],
        "composition": "efficient_readable",
        "atmosphere": "Depression-era practicality, wholesome imagery, value messaging"
    },
    "wartime_1940s": {
        "typography": ["bold_sans", "patriotic_block", "strong_condensed"],
        "decoration": ["stars_stripes", "victory_themes", "minimal_ornament", "ration_messaging"],
        "colors": ["red_white_blue", "kraft_paper_brown", "utilitarian_palette"],
        "composition": "utilitarian_direct",
        "atmosphere": "WWII-era patriotism, utilitarian design, morale-boosting"
    },
    "mid_century_1950s": {
        "typography": ["atomic_age_script", "googie_lettering", "swooping_moderne"],
        "decoration": ["boomerang_shapes", "starbursts", "abstract_modern", "kidney_shapes"],
        "colors": ["turquoise_pink", "avocado_orange", "optimistic_brights", "chrome_accents"],
        "composition": "dynamic_diagonal",
        "atmosphere": "1950s optimism, atomic age energy, modern suburban lifestyle"
    },
    "psychedelic_1960s": {
        "typography": ["groovy_bubble", "op_art_distorted", "flowing_organic"],
        "decoration": ["swirls_paisley", "flower_power", "concentric_patterns", "mandala_forms"],
        "colors": ["neon_saturation", "purple_orange", "acid_brights", "rainbow_spectrum"],
        "composition": "all_over_pattern",
        "atmosphere": "1960s psychedelia, youth culture, vibrant energy, counterculture"
    },
    "retro_1970s": {
        "typography": ["rounded_friendly", "fat_face_serif", "balloon_letters"],
        "decoration": ["rainbow_stripes", "smiley_faces", "geometric_simple", "disco_elements"],
        "colors": ["earth_tones", "harvest_gold", "burnt_orange_brown", "avocado_green"],
        "composition": "centered_bold_simple",
        "atmosphere": "1970s nostalgia, warm earth tones, friendly approachable design"
    }
}

PACKAGE_FORMATS = {
    "twist_wrap": {
        "structure": "cylindrical with twisted ends, candy visible through transparent sections",
        "materials": ["wax_paper", "foil", "cellophane"],
        "typical_candy": ["hard_candies", "taffy", "caramels", "butterscotch"],
        "display": "bulk jar or counter rolls",
        "visual_notes": "twisted end crimps, cylindrical form, often semi-transparent"
    },
    "bar_wrapper": {
        "structure": "flat rectangular fold, inner foil visible at edges",
        "materials": ["foil_inner", "paper_outer", "glassine"],
        "typical_candy": ["chocolate_bars", "nougat_bars", "candy_bars"],
        "display": "counter box or standing rack",
        "visual_notes": "crisp folds, foil shimmer at edges, rectangular proportions"
    },
    "box_and_sleeve": {
        "structure": "inner tray slides into decorative outer sleeve",
        "materials": ["coated_cardboard", "embossed_paper", "die_cut_windows"],
        "typical_candy": ["assorted_chocolates", "premium_confections", "truffles"],
        "display": "shelf facing forward, gift presentation",
        "visual_notes": "dimensional box form, sleeve decoration, possible window showing contents"
    },
    "tin_container": {
        "structure": "hinged or slip-lid metal container with all-over decoration",
        "materials": ["lithographed_tin", "embossed_metal", "printed_label"],
        "typical_candy": ["mints", "hard_candies", "toffees", "lozenges"],
        "display": "counter display or gift tin",
        "visual_notes": "metallic sheen, embossed texture, aged patina, dimensional form"
    },
    "cellophane_bag": {
        "structure": "clear bag with printed header card at top",
        "materials": ["clear_cellophane", "printed_card_top", "twist_tie_or_staple"],
        "typical_candy": ["gummies", "jellies", "wrapped_assortments"],
        "display": "pegboard hanging or counter bin",
        "visual_notes": "transparent bag showing colorful contents, header card decoration"
    },
    "counter_jar": {
        "structure": "glass jar with decorative lid and label",
        "materials": ["clear_glass", "metal_lid", "paper_label"],
        "typical_candy": ["penny_candies", "bulk_confections", "hard_candies"],
        "display": "drugstore or candy shop counter",
        "visual_notes": "cylindrical glass form, contents visible, vintage label design"
    }
}

MATERIAL_VOCABULARY = {
    "foil": {
        "visual": "reflective metallic surface, embossed texture, crisp angular folds catching light",
        "colors": ["gold", "silver", "colored_foil", "bronze"],
        "era_peak": "1920s-1960s",
        "tactile": "smooth metallic, crinkled texture, sharp creases"
    },
    "wax_paper": {
        "visual": "translucent matte finish, soft organic folds, printed flat colors",
        "colors": ["white", "cream", "pastels", "two_color_print"],
        "era_peak": "1900s-1950s",
        "tactile": "waxy smooth, semi-transparent, gentle crinkle"
    },
    "cellophane": {
        "visual": "glossy transparent surface, crinkled texture catching light, tape sealed",
        "colors": ["clear", "tinted", "printed_overlay"],
        "era_peak": "1930s-1970s",
        "tactile": "crisp plastic crinkle, glossy smooth, transparent"
    },
    "lithographed_tin": {
        "visual": "rich printed colors on metal, embossed details, aged patina and wear",
        "colors": ["full_color_illustration", "gold_trim", "vintage_printing"],
        "era_peak": "1890s-1930s",
        "tactile": "solid metal weight, embossed raised details, smooth or textured surface"
    },
    "coated_cardboard": {
        "visual": "matte or glossy coated paper, die-cut windows, visible fold lines",
        "colors": ["vibrant_offset_printing", "spot_colors", "full_color"],
        "era_peak": "1940s-1970s",
        "tactile": "sturdy cardboard, smooth coating, dimensional box structure"
    },
    "embossed_paper": {
        "visual": "raised decorative patterns, textured surface, dimensional details",
        "colors": ["metallic_foil_stamping", "rich_solid_colors"],
        "era_peak": "1890s-1920s",
        "tactile": "textured raised surface, premium paper weight, tactile decoration"
    }
}

TYPOGRAPHY_STYLES = {
    "ornate_victorian": "heavily embellished serif, drop shadows, inline decoration, multiple ornate fonts, decorative capitals",
    "art_nouveau_organic": "flowing organic curves, nature-inspired letterforms, asymmetric layout, whiplash lines",
    "art_deco_geometric": "angular geometric forms, stepped shapes, inline metallic patterns, streamlined serif, vertical emphasis",
    "hand_lettered_casual": "friendly brush script, irregular personal touch, warm hand-drawn quality",
    "atomic_modern": "swooping kinetic scripts, starburst accents, dynamic angles, forward motion",
    "bubble_psychedelic": "rounded inflated bubble letters, distorted op-art effects, groovy organic forms",
    "bold_utilitarian": "strong sans serif impact, maximum legibility, minimal decoration, direct communication",
    "condensed_gothic": "tall narrow letters, economical space usage, strong vertical emphasis",
    "googie_lettering": "space age curves, boomerang accents, atomic starbursts, optimistic energy"
}

BRAND_TONES = {
    "premium_luxury": {
        "cues": ["gold_foil_accents", "embossing", "elegant_script", "French_phrases", "quality_seals"],
        "typical_eras": ["art_nouveau_1900s", "art_deco_1920s"],
        "messaging": "superior quality, refined taste, special occasion, gift-worthy",
        "color_approach": "restrained elegant palette, metallic accents, sophisticated contrast"
    },
    "wholesome_family": {
        "cues": ["hand_drawn_children", "farm_scenes", "mother_figure", "home_made_quality", "wholesome_imagery"],
        "typical_eras": ["depression_1930s", "wartime_1940s", "mid_century_1950s"],
        "messaging": "family tradition, pure ingredients, trusted recipe, home comfort",
        "color_approach": "warm approachable colors, pastoral scenes, comforting palette"
    },
    "novelty_fun": {
        "cues": ["cartoon_mascots", "bright_colors", "exclamation_points", "kid_appeal", "playful_illustration"],
        "typical_eras": ["mid_century_1950s", "psychedelic_1960s", "retro_1970s"],
        "messaging": "fun excitement, kid-friendly, flavor adventure, playful energy",
        "color_approach": "saturated brights, rainbow colors, high contrast, energetic"
    },
    "traditional_heritage": {
        "cues": ["established_date", "family_recipe", "old_world_imagery", "heritage_seals", "classic_typography"],
        "typical_eras": ["victorian_1890s", "art_nouveau_1900s", "depression_1930s"],
        "messaging": "time-tested quality, authentic recipe, generations of expertise",
        "color_approach": "classic colors, burgundy and gold, traditional palette, timeless"
    },
    "modern_progressive": {
        "cues": ["clean_lines", "modern_illustration", "contemporary_style", "innovative_messaging"],
        "typical_eras": ["mid_century_1950s", "psychedelic_1960s", "retro_1970s"],
        "messaging": "new and improved, forward-thinking, contemporary taste",
        "color_approach": "bold modern palette, unexpected combinations, fresh approach"
    }
}

# Display context vocabulary
DISPLAY_CONTEXTS = {
    "counter_display": "vintage store counter perspective, other period products nearby, warm interior lighting",
    "shelf_facing": "straight-on shelf view, multiple packages in row, retail environment",
    "advertisement_view": "clean product shot, promotional angle, idealized presentation",
    "gift_presentation": "special occasion setting, ribbon or wrapping visible, premium context",
    "drugstore_nostalgia": "old pharmacy counter, glass jars and tins, period-appropriate fixtures",
    "candy_shop": "traditional candy store display, bulk containers, nostalgic atmosphere"
}

# ============================================================================
# LAYER 1: INTENT ANALYSIS (Claude call)
# ============================================================================

@mcp.tool()
def analyze_packaging_intent(prompt: str) -> dict:
    """
    Analyze user's prompt to extract packaging intent and preferences.
    
    Claude interprets:
    - Era hints (explicit like "1920s" or implicit like "Art Deco")
    - Candy type (chocolate, hard candy, gummies, etc.)
    - Tone/mood (elegant, playful, premium, nostalgic)
    - Color preferences (if mentioned)
    - Brand personality (luxury, family, novelty, heritage)
    - Any specific style references
    
    Args:
        prompt: User's original prompt or request
        
    Returns:
        JSON dict with extracted intent: {
            "era": "art_deco_1920s",
            "candy_type": "chocolate_bar",
            "tone": "premium_luxury",
            "mood": "elegant, sophisticated",
            "color_hints": ["gold", "black"],
            "brand_tone": "premium_luxury",
            "specific_references": ["Parisian", "geometric"]
        }
        
    Example:
        Input: "1920s luxury chocolate wrapper with gold accents"
        Output: {
            "era": "art_deco_1920s",
            "candy_type": "chocolate_bar",
            "tone": "premium_luxury",
            "mood": "elegant, sophisticated, glamorous",
            "color_hints": ["gold", "black", "metallic"],
            "brand_tone": "premium_luxury",
            "specific_references": ["Parisian style", "geometric patterns"]
        }
    """
    # This tool prompts Claude to analyze and return structured JSON
    return {
        "requires_claude": True,
        "prompt_guidance": f"""Analyze this confection packaging request and return JSON:

User request: {prompt}

Extract and return JSON with these fields:
- era: best matching era key from {list(ERA_STYLES.keys())}
- candy_type: type of candy (chocolate_bar, hard_candies, gummies, etc.)
- tone: overall mood (elegant, playful, premium, nostalgic, fun, traditional)
- mood: descriptive mood words
- color_hints: any mentioned or implied colors (list)
- brand_tone: best matching brand personality from {list(BRAND_TONES.keys())}
- specific_references: any specific style elements mentioned (list)

Return only valid JSON, no other text."""
    }

# ============================================================================
# LAYER 2: DETERMINISTIC MAPPING
# ============================================================================

@mcp.tool()
def map_packaging_parameters(intent_json: str) -> dict:
    """
    Deterministically map intent to visual parameters using taxonomy.
    
    Takes analyzed intent and returns specific visual parameters:
    - Era style details (typography, decoration, colors, composition)
    - Package format specifications
    - Material properties and textures
    - Typography characteristics
    - Brand tone cues
    - Display context
    
    Args:
        intent_json: JSON string from analyze_packaging_intent
        
    Returns:
        Comprehensive parameter mapping for synthesis
        
    Example:
        Input: {"era": "art_deco_1920s", "candy_type": "chocolate_bar", ...}
        Output: Complete visual parameter specification with era styles,
                materials, typography, etc.
    """
    try:
        intent = json.loads(intent_json)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON input"}
    
    # Get era style
    era = intent.get("era", "mid_century_1950s")
    era_style = ERA_STYLES.get(era, ERA_STYLES["mid_century_1950s"])
    
    # Determine package format based on candy type
    candy_type = intent.get("candy_type", "chocolate_bar")
    if "chocolate" in candy_type or "bar" in candy_type:
        format_key = "bar_wrapper"
    elif "hard" in candy_type or "mint" in candy_type or "lozenge" in candy_type:
        format_key = "tin_container"
    elif "gum" in candy_type or "jelly" in candy_type:
        format_key = "cellophane_bag"
    elif "assort" in candy_type or "collection" in candy_type:
        format_key = "box_and_sleeve"
    elif "taffy" in candy_type or "caramel" in candy_type:
        format_key = "twist_wrap"
    else:
        format_key = "bar_wrapper"
    
    package_format = PACKAGE_FORMATS[format_key]
    
    # Get material specs based on format and era
    primary_material = package_format["materials"][0]
    material_specs = MATERIAL_VOCABULARY.get(primary_material, MATERIAL_VOCABULARY["coated_cardboard"])
    
    # Get typography style
    typo_style = era_style["typography"][0]
    typography = TYPOGRAPHY_STYLES.get(typo_style, TYPOGRAPHY_STYLES["bold_utilitarian"])
    
    # Get brand tone
    brand_tone_key = intent.get("brand_tone", "wholesome_family")
    brand_tone = BRAND_TONES.get(brand_tone_key, BRAND_TONES["wholesome_family"])
    
    # Determine display context
    if brand_tone_key == "premium_luxury":
        display_context = DISPLAY_CONTEXTS["gift_presentation"]
    elif format_key == "tin_container":
        display_context = DISPLAY_CONTEXTS["counter_display"]
    elif format_key == "counter_jar":
        display_context = DISPLAY_CONTEXTS["candy_shop"]
    else:
        display_context = DISPLAY_CONTEXTS["shelf_facing"]
    
    # Build comprehensive parameter mapping
    parameters = {
        "era_style": {
            "period": era,
            "typography": era_style["typography"],
            "decoration": era_style["decoration"],
            "colors": era_style["colors"],
            "composition": era_style["composition"],
            "atmosphere": era_style["atmosphere"]
        },
        "package_format": {
            "type": format_key,
            "structure": package_format["structure"],
            "materials": package_format["materials"],
            "display": package_format["display"],
            "visual_notes": package_format["visual_notes"]
        },
        "material_specs": {
            "primary": primary_material,
            "visual": material_specs["visual"],
            "colors": material_specs["colors"],
            "tactile": material_specs["tactile"],
            "era_peak": material_specs["era_peak"]
        },
        "typography": {
            "style_name": typo_style,
            "description": typography
        },
        "brand_tone": {
            "personality": brand_tone_key,
            "cues": brand_tone["cues"],
            "messaging": brand_tone["messaging"],
            "color_approach": brand_tone["color_approach"]
        },
        "display_context": display_context,
        "user_color_hints": intent.get("color_hints", []),
        "mood": intent.get("mood", "nostalgic vintage charm")
    }
    
    return parameters

# ============================================================================
# LAYER 3: CREATIVE SYNTHESIS (Claude call)
# ============================================================================

@mcp.tool()
def synthesize_packaging_prompt(
    base_prompt: str,
    parameters_json: str
) -> dict:
    """
    Final synthesis combining deterministic parameters with creative atmosphere.
    
    Claude takes all mapped parameters and creates cohesive enhanced prompt with:
    - Integrated era-specific atmosphere
    - Material textures and lighting
    - Typography and decoration details
    - Brand personality expression
    - Display context and viewing angle
    - Sensory details (crinkle, shine, patina, wear)
    - Nostalgic qualities
    
    Args:
        base_prompt: Original user prompt
        parameters_json: JSON string from map_packaging_parameters
        
    Returns:
        Final enhanced prompt ready for image generation
        
    Example output structure:
        "A 1920s Art Deco chocolate bar wrapper with geometric sophistication.
        Gold foil inner wrapper visible at crisp folded edges, outer sleeve in
        rich black paper with embossed gold sunburst pattern radiating from
        centered brand name in elegant streamlined serif..."
    """
    try:
        params = json.loads(parameters_json)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON parameters"}
    
    return {
        "requires_claude": True,
        "synthesis_guidance": f"""Create an enhanced image generation prompt for vintage candy packaging.

Original request: {base_prompt}

Use these deterministic parameters:

ERA STYLE ({params['era_style']['period']}):
- Atmosphere: {params['era_style']['atmosphere']}
- Typography: {', '.join(params['era_style']['typography'])}
- Decoration: {', '.join(params['era_style']['decoration'])}
- Colors: {', '.join(params['era_style']['colors'])}
- Composition: {params['era_style']['composition']}

PACKAGE FORMAT ({params['package_format']['type']}):
- Structure: {params['package_format']['structure']}
- Materials: {', '.join(params['package_format']['materials'])}
- Visual notes: {params['package_format']['visual_notes']}

MATERIAL DETAILS:
- Primary material: {params['material_specs']['primary']}
- Visual qualities: {params['material_specs']['visual']}
- Tactile feel: {params['material_specs']['tactile']}

TYPOGRAPHY:
- Style: {params['typography']['style_name']}
- Details: {params['typography']['description']}

BRAND PERSONALITY ({params['brand_tone']['personality']}):
- Visual cues: {', '.join(params['brand_tone']['cues'])}
- Messaging: {params['brand_tone']['messaging']}
- Color approach: {params['brand_tone']['color_approach']}

DISPLAY CONTEXT:
{params['display_context']}

USER MOOD/PREFERENCES:
- Mood: {params['mood']}
- Color hints: {', '.join(params.get('user_color_hints', []))}

Synthesize a detailed image generation prompt that:
1. Opens with the era and package type
2. Describes the material and structural details
3. Integrates typography and decoration specifics
4. Captures the brand personality
5. Includes sensory/tactile qualities (crinkle, shine, wear, patina)
6. Sets the display context and lighting
7. Maintains nostalgic vintage authenticity

Write in prose (not bullet points). Be specific about visual details.
Focus on what makes this era/format distinctive and authentic."""
    }

# ============================================================================
# CONVENIENCE WORKFLOW
# ============================================================================

@mcp.tool()
def enhance_packaging_prompt(original_prompt: str) -> dict:
    """
    Complete three-layer workflow in one call for convenience.
    
    This combines all three steps:
    1. Analyze intent (requires Claude)
    2. Map parameters deterministically
    3. Synthesize final prompt (requires Claude)
    
    Returns workflow guidance showing each step.
    
    Args:
        original_prompt: User's original prompt request
        
    Returns:
        Workflow instructions for completing all three layers
        
    Usage:
        For most efficient use, call the three tools separately:
        1. analyze_packaging_intent()
        2. map_packaging_parameters()
        3. synthesize_packaging_prompt()
        
        This allows you to see and validate the deterministic mapping
        before final synthesis.
    """
    return {
        "workflow_steps": [
            {
                "step": 1,
                "tool": "analyze_packaging_intent",
                "input": original_prompt,
                "purpose": "Claude extracts era, candy type, tone, and preferences"
            },
            {
                "step": 2,
                "tool": "map_packaging_parameters",
                "input": "intent JSON from step 1",
                "purpose": "Deterministic mapping to visual parameters (zero tokens)"
            },
            {
                "step": 3,
                "tool": "synthesize_packaging_prompt",
                "input": "original prompt + parameters JSON from step 2",
                "purpose": "Claude creates final enhanced prompt with full atmosphere"
            }
        ],
        "original_prompt": original_prompt,
        "note": "Call each tool separately for best results and transparency"
    }

# ============================================================================
# EXPLORATION & REFERENCE TOOLS
# ============================================================================

@mcp.tool()
def list_available_eras() -> dict:
    """
    List all available vintage eras with their key characteristics.
    
    Returns:
        Dictionary of eras with descriptions and typical features
    """
    eras = {}
    for era_key, era_data in ERA_STYLES.items():
        eras[era_key] = {
            "atmosphere": era_data["atmosphere"],
            "key_colors": era_data["colors"][:3],
            "decoration_style": era_data["decoration"][:2],
            "composition": era_data["composition"]
        }
    return {"available_eras": eras}

@mcp.tool()
def list_package_formats() -> dict:
    """
    List all available package format types.
    
    Returns:
        Dictionary of package formats with typical candies and materials
    """
    formats = {}
    for format_key, format_data in PACKAGE_FORMATS.items():
        formats[format_key] = {
            "typical_candy": format_data["typical_candy"],
            "materials": format_data["materials"],
            "display": format_data["display"]
        }
    return {"available_formats": formats}

@mcp.tool()
def list_brand_personalities() -> dict:
    """
    List available brand personality types with their characteristics.
    
    Returns:
        Dictionary of brand tones and their typical cues
    """
    personalities = {}
    for tone_key, tone_data in BRAND_TONES.items():
        personalities[tone_key] = {
            "messaging": tone_data["messaging"],
            "visual_cues": tone_data["cues"][:3],
            "typical_eras": tone_data["typical_eras"]
        }
    return {"available_brand_tones": personalities}

@mcp.tool()
def get_era_combinations() -> dict:
    """
    Suggest interesting era + brand tone combinations.
    
    Returns:
        Curated combinations that work well together historically
    """
    combinations = {
        "elegant_victorian": {
            "era": "victorian_1890s",
            "brand_tone": "traditional_heritage",
            "example": "Victorian heritage toffee tin with botanical decoration"
        },
        "art_nouveau_luxury": {
            "era": "art_nouveau_1900s",
            "brand_tone": "premium_luxury",
            "example": "Art Nouveau chocolate box with maiden and floral motifs"
        },
        "deco_glamour": {
            "era": "art_deco_1920s",
            "brand_tone": "premium_luxury",
            "example": "Art Deco gold foil wrapper with geometric sunbursts"
        },
        "depression_wholesome": {
            "era": "depression_1930s",
            "brand_tone": "wholesome_family",
            "example": "Depression-era family candy bar with value messaging"
        },
        "wartime_patriotic": {
            "era": "wartime_1940s",
            "brand_tone": "wholesome_family",
            "example": "WWII candy tin with stars and stripes, morale messaging"
        },
        "atomic_fun": {
            "era": "mid_century_1950s",
            "brand_tone": "novelty_fun",
            "example": "1950s candy with atomic starbursts and space age mascot"
        },
        "psychedelic_novelty": {
            "era": "psychedelic_1960s",
            "brand_tone": "novelty_fun",
            "example": "1960s groovy candy with flower power and rainbow colors"
        },
        "seventies_friendly": {
            "era": "retro_1970s",
            "brand_tone": "wholesome_family",
            "example": "1970s earth tone candy bar with smiley face and rainbows"
        }
    }
    return {"recommended_combinations": combinations}
