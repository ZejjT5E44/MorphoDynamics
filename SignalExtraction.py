import pickle
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from ArtifactGenerator import Plot

def signalExtraction():
   # print(matplotlib.get_configdir())
   # print(matplotlib.matplotlib_fname())
   # quit()

   plot = Plot(True)

   data = pickle.load(open(plot.path + "Signals.pkl", "rb"))

   pdf = PdfPages(plot.path + "Signals.pdf")

   cmax = np.max(np.abs(data['displacement']))

   plot.plotopen('Displacement', 1)
   plt.imshow(data['displacement'], cmap='bwr')
   plt.axis('auto')
   plt.xlabel('Frame index')
   plt.ylabel('Window index')
   plt.colorbar(label='Displacement [pixels]')
   plt.clim(-cmax, cmax)
   # plt.xticks(range(0, velocity.shape[1], 5))
   plot.plotclose(False)
   pdf.savefig()

   # plt.show()

   for m in range(len(data['sigsrc'])):
      plot.plotopen('Signal: ' + data['sigsrc'][m], 1)
      plt.imshow(data['signal'][m], cmap='plasma')
      plt.colorbar(label='Signal')
      plt.axis('auto')
      plt.xlabel('Frame index')
      plt.ylabel('Window index')
      # plt.xticks(range(0, signal.shape[1], 5))
      plot.plotclose(False)
      pdf.savefig()

   pdf.close()