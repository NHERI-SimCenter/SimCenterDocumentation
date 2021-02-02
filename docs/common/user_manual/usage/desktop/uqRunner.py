# written: Michael Gardner @ UNR

# DO NOT CHANGE THE FACTORY, JUST IMPORT IT INTO ADDITIONAL DERIVED CLASSES
# Polymorhophic factory for running UQ apps
class UqRunnerFactory:
    factories = {}
    def addFactory(id, runnerFactory):
        UqRunnerFactory.factories.put[id] = runnerFactory
    addFactory = staticmethod(addFactory)
    # A Template Method:
    def createRunner(id):
        if id not in UqRunnerFactory.factories:
            UqRunnerFactory.factories[id] = \
              eval(id + '.Factory()')
        return UqRunnerFactory.factories[id].create()
    
    createRunner = staticmethod(createRunner)

# Abstract base class
class UqRunner(object):
    def runUQ(self, uqData, simulationData, randomVarsData, demandParams,
              workingDir, runType, localAppDir, remoteAppDir):
        """
        This function configures and runs a UQ simulation based on the 
        input UQ configuration, simulation configuration, random variables,
        and requested demand parameters
        
        Input:
        uqData:         JsonObject that UQ options as input into the quoFEM GUI
        simulationData: JsonObject that contains information on the analysis package to run and its
                    configuration as input in the quoFEM GUI
        randomVarsData: JsonObject that specifies the input random variables, their distributions,
                    and associated parameters as input in the quoFEM GUI
        demandParams:   JsonObject that specifies the demand parameters as input in the quoFEM GUI
        workingDir:     Directory in which to run simulations and store temporary results
        runType:        Specifies whether computations are being run locally or on an HPC cluster
        localAppDir:    Directory containing apps for local run
        remoteAppDir:   Directory containing apps for remote run
        """    
        pass

    # Factory for creating UQ runner
    class Factory:
        def create(self):
            pass
