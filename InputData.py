
# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1         # years

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.00,    0.10],       #WELL
    [0.00,  0.00,   1.00,    0.00],       #STROKE
    [0.00,  0.25,   0.55,    0.20],       #POST STROKE
    [0.00,  0.00,   0.00,    1.00],       #DEATH
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,      # WELL
    5000.0,   # STROKE
    200.0    # POST STROKE
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,      # WELL
    0.2,   # STROKE
    0.9       # POST STROKE
    ]


PSA_ON = False

# annual drug costs
NOTHERAPY_COST = 0.0
ANTICOAG_COST = 2000.0

# No treatment relative risk
NOTREATMENT_RR = 0.50
NOTREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI

ANTICOAG_RR=1.05



