# List of materials
material_dict = [
    "Brick",
    "Cement",
    "Concrete",
    "Glass",
    "Steel",
    "Timber"
]
# Bricks
brick_list = [
    "General",
    "Limestone",
]
brick_type_dict = {
    "General": {
        "embodied energy": "Embodied Energy: 3 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.06 KgC/Kg",
    },
    "Limestone": {
        "embodied energy": "Embodied Energy: 0.85 MJ/Kg",
        "embodied carbon": "Embodied Carbon: nil",
    }
}
# Cement
cement_list = [
    "General", "Portland Cement", "Fibre Cement", "Mortar",
]
cement_type_dict = {
    "General": {
        "embodied energy": "Embodied Energy: 4.6 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.226 KgC/Kg",
    },
    "Portland Cement": {
        "embodied energy": "Embodied Energy: 5.9 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.248 KgC/Kg",
    },
    "Fibre Cement": {
        "embodied energy": "Embodied Energy: 10.9 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.575 KgC/Kg"
    },
    "Mortar (1:3 cement:sand mix)": {
        "embodied energy": "Embodied Energy: 1.4 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.058 KgC/Kg"
    },
    "Mortar (1:1:6 cement:lime:sand mix": {
        "embodied energy": "Embodied Energy: 1.18 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.044 KgC/Kg"
    },
    "Soil Cement": {
        "embodied energy": "Embodied Energy: 0.85 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.038 KgC/Kg"
    },
}

concrete_list = [
    "General", "Precast concrete (cement, sand and aggregates)", "1 :1 :2 (high strength)", "Auto-claved "
                                                                                            "aerated blocks ("
                                                                                            "AACs)",
    "Fibre Reinforced", "Road and Pavement",
]
concrete_dict = {
    "General": {
        "embodied energy": "Embodied Energy: 0.95 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.035 KgC/Kg"
    },
    "Precast concrete (cement, sand and aggregates)": {
        "embodied energy": "Embodied Energy: 2 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.059 KgC/Kg"
    },
    "1 :1 :2 (high strength)": {
        "embodied energy": "Embodied Energy: 1.39 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.057 KgC/Kg"
    },
    "Auto-claved aerated blocks (AACs)": {
        "embodied energy": "Embodied Energy: 3.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.102 KgC/Kg"
    },
    "Fibre Reinforced": {
        "embodied energy": "Embodied Energy: 7.75 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.123 KgC/Kg"
    },
    "Road and Pavement": {
        "embodied energy": "Embodied Energy: 1.25 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.035 KgC/Kg"
    },
}

glass_list = [
    "General (1:2:4)", "Fibre glass (glass-wool)", "Toughened",
]
glass_dict = {
    "General (1:2:4)": {
        "embodied energy": "Embodied Energy: 15 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.232 KgC/Kg"
    },
    "Fibre glass (glass-wool)": {
        "embodied energy": "Embodied Energy: 28 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.417 KgC/Kg"
    },
    "Toughened": {
        "embodied energy": "Embodied Energy: 23.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.346 KgC/Kg"
    },
}

steel_list = [
    "General, ‘typical’ (42.3% recycled content)",
    "General, primary",
    "General, secondary",
    "Bar & rod, ‘typical’ (42.3% recycled content)",
    "Bar & rod, secondary",
    "Engineering steel, secondary",
    "Galvanised sheet, primary",
    "Stainless",
    "Wire",
    "Sheet, primary",
    "Section, ‘typical’ (42.3% recycled content)"
]
steel_dict = {
    "General, ‘typical’ (42.3% recycled content)": {
        "embodied energy": "Embodied Energy: 24.4 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.482 KgC/Kg"
    },
    "General, primary": {
        "embodied energy": "Embodied Energy: 35.3 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.749 KgC/Kg"
    },
    "General, secondary": {
        "embodied energy": "Embodied Energy: 9.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.117 KgC/Kg"
    },
    "Bar & rod, ‘typical’ (42.3% recycled content)": {
        "embodied energy": "Embodied Energy: 24.6 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.466 KgC/Kg"
    },
    "Bar & rod, secondary": {
        "embodied energy": "Embodied Energy: 8.8 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.114 KgC/Kg"
    },
    "Engineering steel, secondary": {
        "embodied energy": "Embodied Energy: 13.1 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.185 KgC/Kg"
    },
    "Galvanised sheet, primary": {
        "embodied energy": "Embodied Energy: 39 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.768 KgC/Kg"
    },
    "Stainless": {
        "embodied energy": "Embodied Energy: 56.7 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 1.676 KgC/Kg"
    },
    "Wire": {
        "embodied energy": "Embodied Energy: 36 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.771 KgC/Kg"
    },
    "Sheet, primary": {
        "embodied energy": "Embodied Energy: 31.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.684 KgC/Kg"
    },
    "Section, ‘typical’ (42.3% recycled content)": {
        "embodied energy": "Embodied Energy: 25.4 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.485 KgC/Kg"
    },
}

timber_list = [
    "General",
    "Glue laminated timber",
    "Hardboard",
    "MDF",
    "Particle board",
    "Plywood",
    "Sawn hardwood",
    "Sawn softwood",
    "Veneer particleboard (furniture)",
]
timber_dict = {
    "General": {
        "embodied energy": "Embodied Energy: 8.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.125 KgC/Kg"
    },
    "Glue laminated timber": {
        "embodied energy": "Embodied Energy: 12 MJ/Kg",
        "embodied carbon": "Embodied Carbon: nil KgC/Kg"
    },
    "Hardboard": {
        "embodied energy": "Embodied Energy: 16 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.234 KgC/Kg"
    },
    "MDF": {
        "embodied energy": "Embodied Energy: 11 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.161 KgC/Kg"
    },
    "Particle board": {
        "embodied energy": "Embodied Energy: 9.5 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.139 KgC/Kg"
    },
    "Plywood": {
        "embodied energy": "Embodied Energy: 15 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.221 KgC/Kg"
    },
    "Sawn hardwood": {
        "embodied energy": "Embodied Energy: 7.8 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.128 KgC/Kg"
    },
    "Sawn softwood": {
        "embodied energy": "Embodied Energy: 7.4 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.123 KgC/Kg"
    },
    "Veneer particleboard (furniture)": {
        "embodied energy": "Embodied Energy: 23 MJ/Kg",
        "embodied carbon": "Embodied Carbon: 0.336 KgC/Kg"
    },
}
