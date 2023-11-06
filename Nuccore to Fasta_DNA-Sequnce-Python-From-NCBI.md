```python
pip install biopython  

```

    Collecting biopython
      Downloading biopython-1.81-cp310-cp310-win_amd64.whl (2.7 MB)
         ---------------------------------------- 2.7/2.7 MB 6.0 MB/s eta 0:00:00
    Requirement already satisfied: numpy in c:\users\melda\anaconda3\lib\site-packages (from biopython) (1.23.5)
    Installing collected packages: biopython
    Successfully installed biopython-1.81
    Note: you may need to restart the kernel to use updated packages.
    

Installing the biopython is crutial step, the reading function of the biopython files is SeqIO.


Then from the https://www.ncbi.nlm.nih.gov/ we can extract the related biomolecular code as FASTA file.

## Load important libraries


```python
from Bio import Entrez
from Bio import SeqIO
```


```python
Entrez.email='melda.elmas@outlook.com'
```

## Download and view the Sequence(Nuccore/ FASTA)


```python
#Data base=nuccore
#Identifier GI number
handle=Entrez.efetch(db='nuccore', id='34577602')

```


```python
print(handle.read())
```

    Seq-entry ::= seq {
      id {
        general {
          db "dbEST",
          tag id 19803415
        },
        genbank {
          accession "CF527907",
          version 1
        },
        gi 34577602
      },
      descr {
        title "UI-1-BC0-aea-d-12-0-UI.s1 NCI_CGAP_Pl1 Homo sapiens cDNA clone
     UI-1-BC0-aea-d-12-0-UI 3'.",
        source {
          org {
            taxname "Homo sapiens",
            common "human",
            db {
              {
                db "National Cancer Institute",
                tag str "UI-1-BC0-aea-d-12-0-UI.s1"
              },
              {
                db "National Cancer Institute",
                tag str "UI-1-BC0-aea-d-12-0-UI"
              },
              {
                db "taxon",
                tag id 9606
              }
            },
            orgname {
              name binomial {
                genus "Homo",
                species "sapiens"
              },
              attrib "specified",
              mod {
                {
                  subtype other,
                  subname "Organ: Placenta; Vector: pT7T3-Pac (Pharmacia) with a
     modified polylinker; Site_1: EcoR I; Site_2: Not I; NCI_CGAP_Pl1 is a cDNA
     library containing the following tissue(s): placenta 8-9 weeks pregnant. The
     library was constructed according to Bonaldo, Lennon and Soares, Genome
     Research, 6:791-806, 1996. First strand cDNA synthesis was primed with an
     oligo-dT primer containing a Not I site. Double stranded cDNA was ligated to
     an EcoR I adaptor, digested with Not I, and cloned directionally into
     pT7T3-Pac vector. The oligonucleotide used to prime the synthesis of
     first-strand cDNA contains a library tag sequence that is located between the
     Not I site and the (dT)18 tail. The sequence tag for this library is GA."
                }
              },
              lineage "Eukaryota; Metazoa; Chordata; Craniata; Vertebrata;
     Euteleostomi; Mammalia; Eutheria; Euarchontoglires; Primates; Haplorrhini;
     Catarrhini; Hominidae; Homo",
              gcode 1,
              mgcode 2,
              div "PRI"
            }
          },
          subtype {
            {
              subtype clone,
              name "UI-1-BC0-aea-d-12-0-UI"
            },
            {
              subtype tissue-type,
              name "Placenta"
            },
            {
              subtype clone-lib,
              name "SAMN00170284 NCI_CGAP_Pl1"
            },
            {
              subtype dev-stage,
              name "8-9 weeks"
            },
            {
              subtype lab-host,
              name "DH10B (Life Technologies)"
            },
            {
              subtype other,
              name "TAG_SEQ=GA"
            },
            {
              subtype other,
              name "TAG_TISSUE=placenta human 8 week"
            },
            {
              subtype other,
              name "TAG_LIB=UI-1-BC0"
            }
          }
        },
        molinfo {
          biomol mRNA,
          tech est
        },
        pub {
          pub {
            gen {
              cit "Unpublished",
              authors {
                names std {
                  {
                    name consortium "NCI-CGAP http://www.ncbi.nlm.nih.gov/ncicgap"
                  }
                }
              },
              date std {
                year 1997
              },
              title "National Cancer Institute, Cancer Genome Anatomy Project
     (CGAP), Tumor Gene Index"
            }
          }
        },
        user {
          type str "DBLink",
          data {
            {
              label str "BioSample",
              num 1,
              data strs {
                "SAMN00170284"
              }
            }
          }
        },
        comment "Contact: Robert Strausberg, Ph.D.~Email:
     cgapbs-r@mail.nih.gov~Tissue Procurement: Dr. Steven Brown~ cDNA Library
     preparation: Dr. M. Bento Soares, University of Iowa~ cDNA Library Arrayed
     by: Dr. M. Bento Soares, University of Iowa~ DNA Sequencing by: Dr. M. Bento
     Soares, University of Iowa~ Clone Distribution: Clone distribution
     information can be obtained from Dr. M. Bento Soares,
     bento-soares@uiowa.edu~~Seq primer: M13 FORWARD~POLYA=Yes",
        create-date std {
          year 2003,
          month 9,
          day 11
        },
        update-date std {
          year 2011,
          month 1,
          day 5
        }
      },
      inst {
        repr raw,
        mol rna,
        length 382,
        strand ss,
        seq-data ncbi2na 'FFFFFF7FD3F9BF3F0112F74013F8B80FA975FEB090285E00C33F000E
    04A40B7D2F4D4E12B32EF57CD3B1FE0915AFFF4CCB7009C820422ECFEEBA0ECFB47E78C1CBE031
    4F355FB045FC20125FF0A4C47BB077DA3F5E73133C48F1300961035130'H
      }
    }
    
    
    


```python
handle=Entrez.efetch(db='nuccore', id='34577602', rettype='fasta')
```


```python
print(handle.read())
```

    >CF527907.1 UI-1-BC0-aea-d-12-0-UI.s1 NCI_CGAP_Pl1 Homo sapiens cDNA clone UI-1-BC0-aea-d-12-0-UI 3', mRNA sequence
    TTTTTTTTTTTTCTTTTCATTTGCGTTTATTTAAACACAGTTCTCAAAACATTTGAGTGAAATTGGGCCT
    CCTTTGGTAAGCAAAGGACCTGAAAATAATATTTAAAAAATGAACAGGCAAAGTCTTCAGTTCATCCATG
    ACAGGTATAGTGTTCCCTTATCATGTACTTTGAAGCACCCGGTTTTTTCATATAGTCTAAAAGCTAGAAG
    AACAAGAGTGTATTTGTGGTGGAATGTATTGTCACTTGCTGATAACTAGTTGAAATACCATTATCCCCTT
    GTAACACCTTTAAGAAACAGCCTTTTAAGGCATACACTGTGTAACTCTTCGGATTTCCTGCTATACATAT
    TACAGATTACATAAAAGCCGACAAATCCACAT
    
    
    


```python
#nucleotide
#identifier: Ascending number
#Output format=Genbank
#Display format=Text
```


```python
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='genbank', retmode='text')
```


```python
print(handle.read())
```

    LOCUS       NM_001126               2775 bp    mRNA    linear   PRI 10-OCT-2010
    DEFINITION  Homo sapiens adenylosuccinate synthase (ADSS), mRNA.
    ACCESSION   NM_001126
    VERSION     NM_001126.2
    KEYWORDS    RefSeq.
    SOURCE      Homo sapiens (human)
      ORGANISM  Homo sapiens
                Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
                Mammalia; Eutheria; Euarchontoglires; Primates; Haplorrhini;
                Catarrhini; Hominidae; Homo.
    REFERENCE   1  (bases 1 to 2775)
      AUTHORS   Sivendran,S. and Colman,R.F.
      TITLE     Effect of a new non-cleavable substrate analog on wild-type and
                serine mutants in the signature sequence of adenylosuccinate lyase
                of Bacillus subtilis and Homo sapiens
      JOURNAL   Protein Sci. 17 (7), 1162-1174 (2008)
       PUBMED   18469177
      REMARK    GeneRIF: Kinetic data reveal that human Ser(289) and B. subtilis
                Ser(262) and Ser(263) are essential for catalysis, while the
                ability of these Ser mutants to bind APBADP suggests that they do
                not contribute to substrate affinity
    REFERENCE   2  (bases 1 to 2775)
      AUTHORS   Zhang,F., Xu,Y., Liu,P., Fan,H., Huang,X., Sun,G., Song,Y. and
                Sham,P.C.
      TITLE     Association analyses of the interaction between the ADSS and ATM
                genes with schizophrenia in a Chinese population
      JOURNAL   BMC Med. Genet. 9, 119 (2008)
       PUBMED   19115993
      REMARK    GeneRIF: These findings suggest that the combined effects of the
                polymorphisms in the ADSS and ATM genes may confer susceptibility
                to the development of schizophrenia in a Chinese population
                GeneRIF: Observational study of gene-disease association and
                gene-gene interaction. (HuGE Navigator)
                Publication Status: Online-Only
    REFERENCE   3  (bases 1 to 2775)
      AUTHORS   Zhang,F., Sham,P.C., Fan,H., Xu,Y., Huang,X., So,H., Song,Y. and
                Liu,P.
      TITLE     An association study of ADSS gene polymorphisms with schizophrenia
      JOURNAL   Behav Brain Funct 4, 39 (2008)
       PUBMED   18721483
      REMARK    GeneRIF: Observational study of gene-disease association. (HuGE
                Navigator)
                Publication Status: Online-Only
    REFERENCE   4  (bases 1 to 2775)
      AUTHORS   Sun,H., Li,N., Wang,X., Chen,T., Shi,L., Zhang,L., Wang,J., Wan,T.
                and Cao,X.
      TITLE     Molecular cloning and characterization of a novel muscle
                adenylosuccinate synthetase, AdSSL1, from human bone marrow stromal
                cells
      JOURNAL   Mol. Cell. Biochem. 269 (1-2), 85-94 (2005)
       PUBMED   15786719
    REFERENCE   5  (bases 1 to 2775)
      AUTHORS   Stepinski,J., Pawelczyk,T., Bizon,D. and Angielski,S.
      TITLE     Purine nucleotide cycle in rat renal cortex and medulla under
                conditions that mimic normal and low oxygen supply
      JOURNAL   Kidney Int. 50 (4), 1195-1201 (1996)
       PUBMED   8887278
    REFERENCE   6  (bases 1 to 2775)
      AUTHORS   Powell,S.M., Zalkin,H. and Dixon,J.E.
      TITLE     Cloning and characterization of the cDNA encoding human
                adenylosuccinate synthetase
      JOURNAL   FEBS Lett. 303 (1), 4-10 (1992)
       PUBMED   1592113
    REFERENCE   7  (bases 1 to 2775)
      AUTHORS   Zalkin,H. and Dixon,J.E.
      TITLE     De novo purine nucleotide biosynthesis
      JOURNAL   Prog. Nucleic Acid Res. Mol. Biol. 42, 259-287 (1992)
       PUBMED   1574589
      REMARK    Review article
    REFERENCE   8  (bases 1 to 2775)
      AUTHORS   Lai,L.W., Hart,I.M. and Patterson,D.
      TITLE     A gene correcting the defect in the CHO mutant Ade -H, deficient in
                a branch point enzyme (adenylosuccinate synthetase) of de novo
                purine biosynthesis, is located on the long arm of chromosome 1
      JOURNAL   Genomics 9 (2), 322-328 (1991)
       PUBMED   2004783
    REFERENCE   9  (bases 1 to 2775)
      AUTHORS   Ogawa,H., Shiraki,H., Matsuda,Y. and Nakagawa,H.
      TITLE     Interaction of adenylosuccinate synthetase with F-actin
      JOURNAL   Eur. J. Biochem. 85 (2), 331-337 (1978)
       PUBMED   648524
    REFERENCE   10 (bases 1 to 2775)
      AUTHORS   Van der Weyden,M.B. and Kelly,W.N.
      TITLE     Human adenylosuccinate synthetase. Partial purification, kinetic
                and regulatory properties of the enzyme from placenta
      JOURNAL   J. Biol. Chem. 249 (22), 7282-7289 (1974)
       PUBMED   4436310
    COMMENT     REVIEWED REFSEQ: This record has been curated by NCBI staff. The
                reference sequence was derived from BC012356.1 and BG700800.1.
                
                [WARNING] On Nov 25, 2010 this sequence was replaced by
                NM_001126.3.
                
                On Sep 11, 2003 this sequence version replaced NM_001126.1.
                
                Summary: Adenylosuccinate synthetase catalyzes the first committed
                step in the conversion of IMP to AMP [provided by RefSeq].
                COMPLETENESS: complete on the 3' end.
    FEATURES             Location/Qualifiers
         source          1..2775
                         /organism="Homo sapiens"
                         /mol_type="mRNA"
                         /db_xref="taxon:9606"
                         /chromosome="1"
                         /map="1cen-q12"
         gene            1..2775
                         /gene="ADSS"
                         /gene_synonym="ADEH; MGC20404"
                         /note="adenylosuccinate synthase"
                         /db_xref="GeneID:159"
                         /db_xref="HGNC:HGNC:292"
                         /db_xref="HPRD:00050"
                         /db_xref="MIM:103060"
         CDS             295..1665
                         /gene="ADSS"
                         /gene_synonym="ADEH; MGC20404"
                         /EC_number="6.3.4.4"
                         /note="adenylosuccinate synthetase
                         (Ade(-)H-complementing); adenylosuccinate synthetase,
                         acidic isozyme; IMP--aspartate ligase 2; adSS 2; AMPSase
                         2; L-type adenylosuccinate synthetase; adenylosuccinate
                         synthetase, liver isozyme"
                         /codon_start=1
                         /product="adenylosuccinate synthetase isozyme 2"
                         /protein_id="NP_001117.2"
                         /db_xref="CCDS:CCDS1624.1"
                         /db_xref="GeneID:159"
                         /db_xref="HGNC:HGNC:292"
                         /db_xref="HPRD:00050"
                         /db_xref="MIM:103060"
                         /translation="MAFAETYPAASSLPNGDCGRPRARPGGNRVTVVLGAQWGDEGKG
                         KVVDLLAQDADIVCRCQGGNNAGHTVVVDSVEYDFHLLPSGIINPNVTAFIGNGVVIH
                         LPGLFEEAEKNVQKGKGLEGWEKRLIISDRAHIVFDFHQAADGIQEQQRQEQAGKNLG
                         TTKKGIGPVYSSKAARSGLRMCDLVSDFDGFSERFKVLANQYKSIYPTLEIDIEGELQ
                         KLKGYMEKIKPMVRDGVYFLYEALHGPPKKILVEGANAALLDIDFGTYPFVTSSNCTV
                         GGVCTGLGMPPQNVGEVYGVVKAYTTRVGIGAFPTEQDNEIGELLQTRGREFGVTTGR
                         KRRCGWLDLVLLKYAHMINGFTALALTKLDILDMFTEIKVGVAYKLDGEIIPHIPANQ
                         EVLNKVEVQYKTLPGWNTDISNARAFKELPVNAQNYVRFIEDELQIPVKWIGVGKSRE
                         SMIQLF"
         regulatory      2732..2737
                         /regulatory_class="polyA_signal_sequence"
                         /gene="ADSS"
                         /gene_synonym="ADEH; MGC20404"
         polyA_site      2757
                         /gene="ADSS"
                         /gene_synonym="ADEH; MGC20404"
    ORIGIN      
            1 ggaaggggcg tggcctcggt ccggggtggc ggccgttgcc gccaccaggg cctcttcctg
           61 cgggcggtgc tgccgaggcc ggcctgcgcg gggcagtcat ggtaccccct tgagcgggct
          121 gtggcggaga gcggggcggg gactggctgg agggtggcgg cccggcgggg cgggggcggg
          181 gccggcctct ggctccttct tcctctgcat gtggctggcg gccgcagagc agttcagttc
          241 gctcactcct cgccggccgc ctctccttcg ggctctcctc gcgtcactgg agccatggcg
          301 ttcgccgaga cctacccggc ggcatcctcc ctgcccaacg gcgattgcgg ccgccccagg
          361 gcgcggcccg gaggaaaccg ggtgacggtg gtgctcggtg cgcagtgggg cgacgaaggc
          421 aaagggaagg tggtggacct gctggcgcag gacgccgaca tcgtgtgccg ctgccaggga
          481 ggaaataatg ctggccatac agttgttgtg gattctgtgg aatatgattt tcatctctta
          541 cccagtggaa taattaatcc aaatgtcact gcattcattg gaaatggtgt ggtaattcat
          601 ctacctggat tgtttgaaga agcagagaaa aatgttcaaa aaggaaaagg actagaaggc
          661 tgggaaaaaa ggcttattat atctgacaga gctcatattg tatttgattt tcatcaagca
          721 gctgatggta tccaggaaca acagagacaa gaacaagcag gaaaaaattt gggtacaaca
          781 aaaaagggca ttggcccagt ttattcgtcc aaagctgctc ggagtggact caggatgtgc
          841 gaccttgttt ctgactttga tggcttctct gagaggttta aagttctagc taaccaatac
          901 aaatctatat accccacttt ggaaatagac attgaaggtg aattacaaaa actcaagggt
          961 tatatggaaa agattaaacc aatggtgaga gatggagttt attttctata tgaggcccta
         1021 catggaccac caaagaaaat cttggtagaa ggtgcaaatg cagcactatt agatattgat
         1081 tttgggactt acccttttgt aacctcttca aattgtactg ttggaggtgt ttgtactggt
         1141 ttgggtatgc cacctcaaaa tgttggagaa gtgtatggag ttgtgaaagc ttatacaact
         1201 agagttggta ttggtgcctt tcctacagag caagacaatg aaattggaga attattacaa
         1261 acaaggggta gagagtttgg tgtaactact ggaaggaaaa gaagatgtgg ctggttggac
         1321 ctcgttttgc tcaaatatgc tcatatgatc aatggattta ctgcgttggc acttaccaag
         1381 ttggatattt tggacatgtt tacggaaatc aaagttggag ttgcttacaa gttagatggt
         1441 gaaatcatac ctcatatccc agcaaaccaa gaagtcttaa ataaagttga agttcaatat
         1501 aagactctcc caggatggaa cacagacata tcaaatgcaa gggcgtttaa agaactacct
         1561 gttaatgcac aaaactatgt tcgatttatt gaagatgagc ttcaaattcc agttaagtgg
         1621 attggtgttg gtaaatccag agaatctatg attcaactct tttaatgatt gccagtaatg
         1681 caagaaacac tccttgagag ggaggggaaa agactttctt aaatatttca tttatgacct
         1741 gcaaattcaa gaataaagac actgaagtaa gtttgaagcc ctacagttgt ttccagtctt
         1801 ttcagatgga tgcctactgt ggagattaac tttggcatat tccagtgtca gctttcttta
         1861 gctggaattg ccaaatcatt tgttgctcct gctgctctca tggtgccacg tttttttttt
         1921 caatgtttag taatagtata atccatgttg tttgatatca aaagtagaat tacttttaat
         1981 gtagtttttc ttcattattg tcattgcgtg ttcttaagtt ttacccctat tagatggtaa
         2041 gaacaattaa tgcagttttg cacaaatatt tttacattct gatcattcag ttctgtcatt
         2101 gtaatctttg ttgttagaaa caaatgatga aaacataggg gttctgtaaa cttttgtaat
         2161 gctatgaatt ctgtttaaat tttgggctgt ctattttctg ctgaaaccat gcaaaattga
         2221 gctttggtgg ggctgggagg gggttatgta ttcatgggac ctttaatttg tacagaacac
         2281 agaacttatt tctgtcagtt atttaataca ttgaaaattt agtgaaatgt tcaaagagaa
         2341 tagatgtttc ccaaaacaac aatctttatg ttaaaaatag tcattaaaag atctgttgta
         2401 atatatggtg gatatttttc tttaatttca aacattacct ctgaaatgtg tatcttttct
         2461 tttttatctt accattaatt ttaaatctag tggattggtt ttcaacatcg tgcctgccga
         2521 tatgcctaca gaatcatctg taagtgtcaa aatgaaccca cgttgttagc cataattttg
         2581 attatgcctt tatttctcct ttcttgaaaa aaaaaaggtg ttattttgac aattaggcat
         2641 aacattgttt tgtagattat cttttaatga actattttaa atgttaaatt aggtgccact
         2701 taaatttatt ttattacacc atgaatagct gattaaaaga accaaatatt tctagtaaaa
         2761 aaaaaaaaaa aaaaa
    //
    
    
    

## Dowloading and Exploring Sequences


```python
#identifier: Ascending number
#Output format=FASTA
#Display format=Text
#data base=nucleotide
```


```python
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='fasta', retmode='text')
```


```python
record=SeqIO.read(handle,'fasta')
```


```python
#sequence id
record.id
```




    'NM_001126.2'




```python
#sequence description
record.description
```




    'NM_001126.2 Homo sapiens adenylosuccinate synthase (ADSS), mRNA'




```python
record.name
```




    'NM_001126.2'




```python
#sequence
seq=record.seq
```


```python
print(seq[0:10])
```

    GGAAGGGGCG
    


```python
#length of the mRNA sequence
len(seq)
```




    2775




```python
print(seq)
```

    GGAAGGGGCGTGGCCTCGGTCCGGGGTGGCGGCCGTTGCCGCCACCAGGGCCTCTTCCTGCGGGCGGTGCTGCCGAGGCCGGCCTGCGCGGGGCAGTCATGGTACCCCCTTGAGCGGGCTGTGGCGGAGAGCGGGGCGGGGACTGGCTGGAGGGTGGCGGCCCGGCGGGGCGGGGGCGGGGCCGGCCTCTGGCTCCTTCTTCCTCTGCATGTGGCTGGCGGCCGCAGAGCAGTTCAGTTCGCTCACTCCTCGCCGGCCGCCTCTCCTTCGGGCTCTCCTCGCGTCACTGGAGCCATGGCGTTCGCCGAGACCTACCCGGCGGCATCCTCCCTGCCCAACGGCGATTGCGGCCGCCCCAGGGCGCGGCCCGGAGGAAACCGGGTGACGGTGGTGCTCGGTGCGCAGTGGGGCGACGAAGGCAAAGGGAAGGTGGTGGACCTGCTGGCGCAGGACGCCGACATCGTGTGCCGCTGCCAGGGAGGAAATAATGCTGGCCATACAGTTGTTGTGGATTCTGTGGAATATGATTTTCATCTCTTACCCAGTGGAATAATTAATCCAAATGTCACTGCATTCATTGGAAATGGTGTGGTAATTCATCTACCTGGATTGTTTGAAGAAGCAGAGAAAAATGTTCAAAAAGGAAAAGGACTAGAAGGCTGGGAAAAAAGGCTTATTATATCTGACAGAGCTCATATTGTATTTGATTTTCATCAAGCAGCTGATGGTATCCAGGAACAACAGAGACAAGAACAAGCAGGAAAAAATTTGGGTACAACAAAAAAGGGCATTGGCCCAGTTTATTCGTCCAAAGCTGCTCGGAGTGGACTCAGGATGTGCGACCTTGTTTCTGACTTTGATGGCTTCTCTGAGAGGTTTAAAGTTCTAGCTAACCAATACAAATCTATATACCCCACTTTGGAAATAGACATTGAAGGTGAATTACAAAAACTCAAGGGTTATATGGAAAAGATTAAACCAATGGTGAGAGATGGAGTTTATTTTCTATATGAGGCCCTACATGGACCACCAAAGAAAATCTTGGTAGAAGGTGCAAATGCAGCACTATTAGATATTGATTTTGGGACTTACCCTTTTGTAACCTCTTCAAATTGTACTGTTGGAGGTGTTTGTACTGGTTTGGGTATGCCACCTCAAAATGTTGGAGAAGTGTATGGAGTTGTGAAAGCTTATACAACTAGAGTTGGTATTGGTGCCTTTCCTACAGAGCAAGACAATGAAATTGGAGAATTATTACAAACAAGGGGTAGAGAGTTTGGTGTAACTACTGGAAGGAAAAGAAGATGTGGCTGGTTGGACCTCGTTTTGCTCAAATATGCTCATATGATCAATGGATTTACTGCGTTGGCACTTACCAAGTTGGATATTTTGGACATGTTTACGGAAATCAAAGTTGGAGTTGCTTACAAGTTAGATGGTGAAATCATACCTCATATCCCAGCAAACCAAGAAGTCTTAAATAAAGTTGAAGTTCAATATAAGACTCTCCCAGGATGGAACACAGACATATCAAATGCAAGGGCGTTTAAAGAACTACCTGTTAATGCACAAAACTATGTTCGATTTATTGAAGATGAGCTTCAAATTCCAGTTAAGTGGATTGGTGTTGGTAAATCCAGAGAATCTATGATTCAACTCTTTTAATGATTGCCAGTAATGCAAGAAACACTCCTTGAGAGGGAGGGGAAAAGACTTTCTTAAATATTTCATTTATGACCTGCAAATTCAAGAATAAAGACACTGAAGTAAGTTTGAAGCCCTACAGTTGTTTCCAGTCTTTTCAGATGGATGCCTACTGTGGAGATTAACTTTGGCATATTCCAGTGTCAGCTTTCTTTAGCTGGAATTGCCAAATCATTTGTTGCTCCTGCTGCTCTCATGGTGCCACGTTTTTTTTTTCAATGTTTAGTAATAGTATAATCCATGTTGTTTGATATCAAAAGTAGAATTACTTTTAATGTAGTTTTTCTTCATTATTGTCATTGCGTGTTCTTAAGTTTTACCCCTATTAGATGGTAAGAACAATTAATGCAGTTTTGCACAAATATTTTTACATTCTGATCATTCAGTTCTGTCATTGTAATCTTTGTTGTTAGAAACAAATGATGAAAACATAGGGGTTCTGTAAACTTTTGTAATGCTATGAATTCTGTTTAAATTTTGGGCTGTCTATTTTCTGCTGAAACCATGCAAAATTGAGCTTTGGTGGGGCTGGGAGGGGGTTATGTATTCATGGGACCTTTAATTTGTACAGAACACAGAACTTATTTCTGTCAGTTATTTAATACATTGAAAATTTAGTGAAATGTTCAAAGAGAATAGATGTTTCCCAAAACAACAATCTTTATGTTAAAAATAGTCATTAAAAGATCTGTTGTAATATATGGTGGATATTTTTCTTTAATTTCAAACATTACCTCTGAAATGTGTATCTTTTCTTTTTTATCTTACCATTAATTTTAAATCTAGTGGATTGGTTTTCAACATCGTGCCTGCCGATATGCCTACAGAATCATCTGTAAGTGTCAAAATGAACCCACGTTGTTAGCCATAATTTTGATTATGCCTTTATTTCTCCTTTCTTGAAAAAAAAAAGGTGTTATTTTGACAATTAGGCATAACATTGTTTTGTAGATTATCTTTTAATGAACTATTTTAAATGTTAAATTAGGTGCCACTTAAATTTATTTTATTACACCATGAATAGCTGATTAAAAGAACCAAATATTTCTAGTAAAAAAAAAAAAAAAAAAA
    


```python
#identifier: Ascending number
#Output format=genbank
#Display format=Text
#data base=nucleotide
```


```python
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2', rettype='gb', retmode='text')
```


```python
record=SeqIO.read(handle,'gb')
```


```python
record.id
```




    'NM_001126.2'




```python
features=record.features
```


```python
len(features)

```




    5




```python
seq=record.seq
```


```python
print(len(seq))
```

    2775
    

## Now, you can download multiple genomes


```python
handle=Entrez.efetch(db='nuccore', id='3457706,186972394', rettype='fasta')
```


```python
print(handle.read())
```

    >AQ088795.1 HS_3002_A1_F10_MF CIT Approved Human Genomic Sperm Library D Homo sapiens genomic clone Plate=3002 Col=19 Row=K, genomic survey sequence
    TAACAAGAGACTTCTGAAGAAAAGAGACATGTCACCCTAGACAATGCTGTTTATGGGGAGTATCTGTATA
    AGGTTGGAAAAGATAATTTCTTAATACTAATTTGCAGAATGGATATTATCTTTAAACAAAATAGATGCCT
    TTTTTGTCAATATAGAATTGGACCTCCAATTGGCTATTTAGAAACATTATAATTGTCTATACTGAACATT
    AAGTAGAAGTAACTTTAAAGCGCATAAGTCAACCTATTTCTCCCTATCAAGAGTGTTGTCAAACTTACAA
    CGAGCAGTTTC
    
    >EU490707.1 Selenipedium aequinoctiale maturase K (matK) gene, partial cds; chloroplast
    ATTTTTTACGAACCTGTGGAAATTTTTGGTTATGACAATAAATCTAGTTTAGTACTTGTGAAACGTTTAA
    TTACTCGAATGTATCAACAGAATTTTTTGATTTCTTCGGTTAATGATTCTAACCAAAAAGGATTTTGGGG
    GCACAAGCATTTTTTTTCTTCTCATTTTTCTTCTCAAATGGTATCAGAAGGTTTTGGAGTCATTCTGGAA
    ATTCCATTCTCGTCGCAATTAGTATCTTCTCTTGAAGAAAAAAAAATACCAAAATATCAGAATTTACGAT
    CTATTCATTCAATATTTCCCTTTTTAGAAGACAAATTTTTACATTTGAATTATGTGTCAGATCTACTAAT
    ACCCCATCCCATCCATCTGGAAATCTTGGTTCAAATCCTTCAATGCCGGATCAAGGATGTTCCTTCTTTG
    CATTTATTGCGATTGCTTTTCCACGAATATCATAATTTGAATAGTCTCATTACTTCAAAGAAATTCATTT
    ACGCCTTTTCAAAAAGAAAGAAAAGATTCCTTTGGTTACTATATAATTCTTATGTATATGAATGCGAATA
    TCTATTCCAGTTTCTTCGTAAACAGTCTTCTTATTTACGATCAACATCTTCTGGAGTCTTTCTTGAGCGA
    ACACATTTATATGTAAAAATAGAACATCTTCTAGTAGTGTGTTGTAATTCTTTTCAGAGGATCCTATGCT
    TTCTCAAGGATCCTTTCATGCATTATGTTCGATATCAAGGAAAAGCAATTCTGGCTTCAAAGGGAACTCT
    TATTCTGATGAAGAAATGGAAATTTCATCTTGTGAATTTTTGGCAATCTTATTTTCACTTTTGGTCTCAA
    CCGTATAGGATTCATATAAAGCAATTATCCAACTATTCCTTCTCTTTTCTGGGGTATTTTTCAAGTGTAC
    TAGAAAATCATTTGGTAGTAAGAAATCAAATGCTAGAGAATTCATTTATAATAAATCTTCTGACTAAGAA
    ATTCGATACCATAGCCCCAGTTATTTCTCTTATTGGATCATTGTCGAAAGCTCAATTTTGTACTGTATTG
    GGTCATCCTATTAGTAAACCGATCTGGACCGATTTCTCGGATTCTGATATTCTTGATCGATTTTGCCGGA
    TATGTAGAAATCTTTGTCGTTATCACAGCGGATCCTCAAAAAAACAGGTTTTGTATCGTATAAAATATAT
    ACTTCGACTTTCGTGTGCTAGAACTTTGGCACGGAAACATAAAAGTACAGTACGCACTTTTATGCGAAGA
    TTAGGTTCGGGATTATTAGAAGAATTCTTTATGGAAGAAGAA
    
    
    


```python
handle=Entrez.efetch(db='nuccore', id='3457706,186972394', rettype='fasta')
```


```python
records=SeqIO.parse(handle,'fasta')
```


```python
records=[i for i in records]
```


```python
len(records)
```




    2




```python
first_record=records[0]
second_record=records[1]
```


```python
first_record.id
```




    'AQ088795.1'




```python
second_record.id
```




    'EU490707.1'




```python
handle=Entrez.efetch(db='nucleotide', id='34577062', rettype='gb')
record=SeqIO.read(handle,'gb')
outputname='/home/kobina/Desktop/ADSS.gb'
```
