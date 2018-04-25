import ParameterClassesTreatment as PT
import ParameterClasses as P
import SupportMarkovModel as SupportMarkov
import MarkovModel as MarkovCls

cohort_notherapy=MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NOTHERAPY
)
simOutputs_notherapy=cohort_notherapy.simulate()

cohort_anticoag=MarkovCls.Cohort(
    id=1,
    therapy=PT.Therapies.ANTICOAG
)
simOutputs_anticoag=cohort_anticoag.simulate()


# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_notherapy, simOutputs_anticoag)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_notherapy, "No Therapy:")
SupportMarkov.print_outcomes(simOutputs_anticoag, "Anticoag Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_notherapy, simOutputs_anticoag)

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_notherapy, simOutputs_anticoag)

#I would recommend paying $0.00 for the adoption of this anticoagulation therapy.