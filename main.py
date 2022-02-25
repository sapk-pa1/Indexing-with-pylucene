file_path= 'datasets/wiki_movie_plots_deduped.csv'
'''
Importing all the required Libraries 
'''
import pandas as pd 
import lucene 
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, StringField, FieldType
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory , FSDirectory 
import org.apache.lucene.document as document
from java.io import StringReader
from org.apache.lucene.analysis.tokenattributes import CharTermAttribute
from org.apache.lucene.analysis.en import EnglishAnalyzer 
from org.apache.lucene.analysis.core import WhitespaceAnalyzer, SimpleAnalyzer , StopAnalyzer 
from java.io import File 

lucene.initVM()#initializing the virtual machine to access the java packages  
def indexSingleMovie(title, plot):
    doc = document.Document()#storing data in lucene understandable format 
    doc.add(document.Field('TITLE', title, document.TextField.TYPE_STORED))
    doc.add(document.Field('PLOT', plot, document.TextField.TYPE_STORED))
    writer.addDocument(doc)
#processing the inverted index 
def make_inverted_index(file_path):
    df = pd.read_csv(file_path)
    doc_id = 0
    for i in df.index:
        print(doc_id, '->', df['Title'][i])
        indexSingleMovie(df['Title'][i], df['Plot'][i])
        doc_id+=1
def closeWriter():
    writer.close()
'''

Writing the index 

'''
indexPath = File("index/").toPath()
indexDir= FSDirectory.open(indexPath)
# set the index writer config 
writerConfig = IndexWriterConfig(EnglishAnalyzer())
#setup another object resposible for writing lucene docs to the dir 
writer = IndexWriter(indexDir, writerConfig)

make_inverted_index(file_path)
closeWriter()