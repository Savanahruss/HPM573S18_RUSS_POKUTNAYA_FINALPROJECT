import ParameterClassesTreatment as P
import MarkovModelTreatment as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

#Create a cohort that receives anticoag therapy
cohort=MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)

#simulate cohort with anticoag therapy
simOutputs=cohort.simulate()

#Graph survival curve of those who receive anticoag therapy
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival Curve of Those With Therapy',
    x_label='Simulation time step',
    y_label='Number of alive patients')

#Graph histogram of survival times of those with therapy
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with Therapy',
    x_label='Survival Time (years)',
    y_label='Counts',
    bin_width=1
)

#print the outcomes of the simulated cohort with therapy
SupportMarkov.print_outcomes(simOutputs, 'With Therapy')