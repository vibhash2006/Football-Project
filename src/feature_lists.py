misc_features = [
    "player",
    "team",
    "league",
    "nation",
    "season",
    "pos",
    "age"
]

availability_features = [
    "age",
    "Playing Time_Min",
    "Playing Time_MP",
    "Playing Time_90s",
    "Starts_Starts"
]

fw_features = [
    # Goals
    "Per 90 Minutes_Gls",
    "Per 90 Minutes_Ast",
    "Per 90 Minutes_G+A",

    # xG / xA
    "xg_per90",
    "xa_per90",

    # Shooting
    "Standard_Sh/90",
    "Standard_SoT/90",
    "sot_ratio",
    "xg_per_shot",

    # Finishing quality
    "shot_conversion",
    "goals_minus_xg",

    # Creation
    "key_passes_per90",

    # Involvement
    "xg_chain_per90",
    "xg_buildup_per90",
    "finishing_share",
    "buildup_share"
]

mf_features = [
    # Goal threat
    "Per 90 Minutes_Gls",
    "xg_per90",

    # Creativity
    "Per 90 Minutes_Ast",
    "xa_per90",
    "key_passes_per90",

    # Involvement
    "xg_chain_per90",
    "xg_buildup_per90",

    # Role indicators
    "finishing_share",
    "buildup_share",

    # Shooting
    "Standard_Sh/90",
    "Standard_SoT/90",

    # Team context
    "Team Success_PPM",
    "Team Success_On-Off"
]

df_features = [
    # Attacking contribution
    "Per 90 Minutes_Gls",
    "Per 90 Minutes_Ast",

    "xg_per90",
    "xa_per90",

    "key_passes_per90",

    # Involvement
    "xg_chain_per90",
    "xg_buildup_per90",

    # Team defensive context
    "Team Success_onGA",
    "Team Success_+/-90",
    "Team Success_On-Off",

    # Discipline
    "Performance_CrdY",
    "Performance_CrdR"
]

gk_features = [
    # Shot stopping
    "Performance_Save%",
    "Performance_Saves",
    "Performance_SoTA",

    # Goals conceded
    "Performance_GA",
    "Performance_GA90",

    # Clean sheets
    "Performance_CS",
    "Performance_CS%",

    # Penalties
    "Penalty Kicks_PKA",
    "Penalty Kicks_PKsv",
    "Penalty Kicks_Save%"
]