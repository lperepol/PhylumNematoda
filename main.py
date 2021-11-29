# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphviz import Digraph
def draw():

    g = Digraph('Nematoda Key', comment="FOO",filename = 'NematodaKey.gv')#, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g.graph_attr['rankdir'] = 'LR'


    g.node('001', label='Phylum\nNematoda',fillcolor='red',style="filled")
    g.node('Class\nChromadorea', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")
    g.node('Class\nEnoplea', shape='doubleoctagon', color='blue', fillcolor='aquamarine3',style="rounded,filled")

    g.edge('001','Amphids')
    g.edge('001','Cuticle')
    g.edge('001','Phasmids')
    g.edge('001','Esophagus')
    g.edge('001','Excretory\nSystem')
    g.edge('001','Females')
    g.edge('001','Caudal\nAlae')
    g.edge('001','Males')


    g.edge('Amphids','Class\nChromadorea', label='Labial\npost-labial\npore-like\nslit-like\nelaborate coils\nspirals')
    g.edge('Cuticle','Class\nChromadorea', label='annulated\nornamented with\nprojections and setae.')
    g.edge('Phasmids','Class\nChromadorea', label='Distinct\nor indistinct\nposterior')
    g.edge('Esophagus','Class\nChromadorea', label='Divided into bulbs\n3 to 5 esophageal glands')
    g.edge('Excretory\nSystem','Class\nChromadorea', label='Glandular\nor tubular.')
    g.edge('Females','Class\nChromadorea', label='One or\n two ovaries.')
    g.edge('Caudal\nAlae','Class\nChromadorea', label='Present or\nabsent')

    g.edge('Amphids','Class\nEnoplea', label='Pocket like\nnot spiral\npost-labial')
    g.edge('Cuticle','Class\nEnoplea', label='Smooth or\nfinely striated')
    g.edge('Phasmids','Class\nEnoplea', label='Present or\nabsent')
    g.edge('Esophagus','Class\nEnoplea', label='Cylindrical or bottle-shaped\n3 to 5 esophageal glands\nstichosome\nor trophosome')
    g.edge('Excretory\nSystem','Class\nEnoplea', label='Simple non-tubular\nSingle cell')
    g.edge('Females','Class\nEnoplea', label='Two ovaries')
    g.edge('Males','Class\nEnoplea', label='Two testes.')
    g.edge('Caudal\nAlae','Class\nEnoplea', label='Rare')



    g.render('NematodaKey.gv', format='svg', view=True)
    g.render('NematodaKey.gv', format='jpg', view=False)
    g.render('NematodaKey.gv', format='pdf', view=False)

def main():
    # Use a breakpoint in the code line below to debug your script.
    draw()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
