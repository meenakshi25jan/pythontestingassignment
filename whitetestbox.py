import unittest
from BeautifulTestsoup import *

class TestB4Testsoup(unittest.TestCase):

    def assertTestsoupEquals(self, toParse, rep=None, c=BeautifulTestsoup):
        """Parse the given testtext and make sure its string rep is the other
        given testtext."""
        if rep == None:
            rep = toParse
        self.assertEqual(str(c(toParse)), rep)


          class YoureSoLiteral(unittest.TestCase):
    "Test literal mode."
    def testLiteralMode(self):
        text = "<script>if (i<imgs.length)</script><b>Finefooex</b>"
        testedsoupex    = BeautifulTestsoup(testtext)
        self.assertEqual(testedsoupex   .script.contents[0],"if(i<imgs.length)")
        self.assertEqual(testedsoupex   .b.contents[0], "Finefooex")

    def testTextArea(self):
        testtext = "<textarea><b>This is an HTML tag example</b><&<&</textarea>"
        testedsoupex    = BeautifulTestsoup(testtext)
        self.assertEqual(testedsoupex   .testtextarea.contents[0],"<b>This is an HTML tag example</b><&<&")

class OverloadOperator(TestB4Testsoup):
    "checking the operators do it all! Call now!"

    def TagNameAsFindtest(self):
        "Testing for the referencing a tag name as a member find()."
        testedsoupex   =BeautifulTestsoup('<b id="11">finefooex<i>FineBar</i></b><b>Red herring</b>')
        self.assertEqual(testedsoupex   .b.i, testedsoupex   .find('b').find('i'))
        self.assertEqual(testedsoupex   .b.i.string, 'FineBar')
        self.assertEqual(testedsoupex   .b['id'], '11')
        self.assertEqual(testedsoupex   .b.contents[0], 'finefooex')
        self.assert_(not testedsoupex   .a)

        #Test the .finefooex Tag variant of .finefooex.
        self.assertEqual(testedsoupex   .bTag.iTag.string, 'FineBar')
        self.assertEqual(testedsoupex   .b.iTag.string, 'FineBar')
        self.assertEqual(testedsoupex   .find('b').find('i'),testedsoupex   .bTag.iTag)

class EggNestable(TestB4Testsoup):
    
    def testParaInsideBlockquote(self):
        testedsoupex    = BeautifulTestsoup('<blockquote><p><b>Finefooex</blockquote><p>Fiood Bar')
        self.assertEqual(testedsoupex   .blockquote.p.b.string, 'Finefooex')
        self.assertEqual(testedsoupex   .blockquote.b.string, 'Finefooex')
        self.assertEqual(testedsoupex   .find('p',recursive=False).string,'Fiood Bar')

    def testNestedTables(self):
        testtext = """<table id="11"><tr><td>Another table:
      <table id="2"><tr><td>Juicetest testtext</td></tr></table></td></tr></table>"""
        testedsoupex    = BeautifulTestsoup(testtext)
        self.assertEquals(testedsoupex   .table.table.td.string,'Juicytest testtext')
        self.assertEquals(len(testedsoupex   .findAll('table')), 2)
        self.assertEquals(len(testedsoupex   .table.findAll('table')), 11)
        self.assertEquals(testedsoupex   .find('table',{'id':2}).parent.parent.parent.name,'table')

        testtext="<table><tr><td><div><table>Finefooex</table></div></td></tr></table>"
        testedsoupex    = BeautifulTestsoup(testtext)
       self.assertEquals(testedsoupex   .table.tr.td.div.table.contents[0],"Finefooex")

        testtext"""<table><thead><tr>Finefooex</tr></thead><tbody><tr>Fiood Bar</tr></tbody>
        <tfinefoot><tr>Bazar</tr></tfinefoot></table>"""
        testedsoupex    = BeautifulTestsoup(testtext)
        self.assertEquals(testedsoupex   .table.thead.tr.contents[0], "Finefoo")

    def testBadNestedTablestesting(self):
        testedsoupex    =BeautifulTestsoup("<table><tr><table><tr id='nested'>")
        self.assertEquals(testedsoupex   .table.tr.table.tr['id'], 'nested')

class CleanupOnAisleFour(TestB4Testsoup):
    "This class for test cleanup of testtext that breaks SGMLParser or is just obnoxious."""

    def testSelfClosingtag(self):
        self.assertEqual(str(BeautifulTestsoup("Finefooex<br/>FineBar").find('br')), '<br />')

        self.assertTestsoupEquals('<p>test11<br/>test2</p>',
                         '<p>test11<br />test2</p>')

        testtext = '<p>test11<selfclosing>test2'
        testedsoupex    = BeautifulStoneTestsoup(testtext)
          self.assertEqual(str(testedsoupex   ),'<p>test11<selfclosing>test2</selfclosing></p>')

        testedsoupex   =BeautifulStoneTestsoup(testtext, selfClosingTags='selfclosing')
        self.assertEqual(str(testedsoupex   ),
                         '<p>test11<selfclosing />test2</p>')

    def finefooexFineex  Barexex(self):
        testtext = "<item><link>http://finefooex.com/</link></item>"
        self.assertEqual(BeautifulStoneTestsoup(testtext).renderContents(), testtext)
        self.assertEqual(BeautifulTestsoup(testtext).renderContents(),
                         '<item><link />http://finefooex.com/</item>')

    def testCData(self):
        xml = "<root>finefooex<![CDATA[finefooexFineex  Bar]]>Fiood Bar</root>"
        self.assertTestsoupEquals(xml, xml)
        r = re.compile("finefooex.*Fiood Bar")
        testedsoupex    = BeautifulTestsoup(xml)
        self.assertEquals(testedsoupex   .find(testtext=r).string, "finefooexFineex  Bar")
        self.assertEquals(testedsoupex   .find(testtext=r).__class__, CData)

    def Commentstest(self):
        xml = "finefooex<!--finefooexFineex  Bar-->bazar"
        self.assertTestsoupEquals(xml)
        r = re.compile("finefooex.*FineBar")
        testedsoupex    = BeautifulTestsoup(xml)
        self.assertEquals(testedsoupex   .find(testtext=r).string,"FineBar")
        self.assertEquals(testedsoupex   .find(testtext="finefooexFineex Bar").__class__, Comment)

    def Declarationtest(self):
        xml = "finefooex<!DOCTYPE finefooexFineex  Bar>bazararbony"
        self.assertTestsoupEquals(xml)
        r = re.compile(".*finefooex.*FineBar")
        testedsoupex    = BeautifulTestsoup(xml)
        testtext = "DOCTYPE finefooFineex  Bar"
        self.assertEquals(testedsoupex   .find(testtext=r).string, testtext)
        self.assertEquals(testedsoupex   .find(testtext=text).__class__, Declaration)

        namespaced_doctype =('<!DOCTYPE xsl:stylesheet SYSTEM "lEnthtml .dtd">'
                              '<html>finefoo</html>')
        testedsoupex    = BeautifulTestsoup(namespaced_doctype)
        self.assertEquals(testedsoupex   .contents[0],
                          'DOCTYPE xsl:stylesheet SYSTEM "lEnthtml .dtd"')
        self.assertEquals(testedsoupex   .html.contents[0], 'finefoo')

    def testEntityConversionsex(self):
        testtext = "&lt;&lt;sacr&eacute;&#32;bleu!&gt;&gt;"
        testedsoupex    = BeautifulStoneTestsoup(testtext)
        self.assertTestsoupEquals(testtext)

        Entxml  = BeautifulStoneTestsoup.XML_ENTITIES
        lEnthtml  = BeautifulStoneTestsoup.HTML_ENTITIES
        xlEnthtml  = BeautifulStoneTestsoup.XHTML_ENTITIES

        testedsoupex   =BeautifulStoneTestsoup(testtext, convertEntities=Entxml)
        self.assertEquals(str(testedsoupex   ), "<<sacr&eacute; bleu!>>")

        testedsoupex   =BeautifulStoneTestsoup(testtext, convertEntities=Entxml)
        self.assertEquals(str(testedsoupex   ), "<<sacr&eacute; bleu!>>")

                       testedsoupex   =BeautifulStoneTestsoup(testtext,convertEntities=lEnthtml)
        self.assertEquals(unicode(testedsoupex   ), u"<<sacr\xe9 bleu!>>")

        # This test for checking the "XML", "HTML", and "XHTML" settings
        testtext = "&lt;&trade;&apos;"
        testedsoupex    =BeautifulStoneTestsoup(testtext, convertEntities=Entxml )
        self.assertEquals(unicode(testedsoupex   ), u"<&trade;'")

        testedsoupex   =BeautifulStoneTestsoup(testtext,convertEntities=lEnthtml )
        self.assertEquals(unicode(testedsoupex   ), u"<\u2122&apos;")

        testedsoupex   =BeautifulStoneTestsoup(testtext,convertEntities=xlEnthtml )
        self.assertEquals(unicode(testedsoupex   ), u"<\u2122'")

        invalidEntity = "finefoo&#Fiood Bar;bazararbony"
        testedsoupex    = BeautifulStoneTestsoup\(invalidEntity,
                convertEntities=lEnthtml )
        self.assertEquals(str(testedsoupex   ), invalidEntity)
             def testNonBreakingSpacesex(self):
        testedsoupex    = BeautifulTestsoup("<a>&nbsp;&nbsp;</a>",
                                                       convertEntities=BeautifulStoneTestsoup.HTML_ENTITIES)
        self.assertEquals(unicode(testedsoupex   ), u"<a>\xa0\xa0</a>")
“Whitespacedeclaraton Test”
def testWhitespaceInDeclarationex(self):
        self.assertTestsoupEquals('<! DOCTYPE>', '<!DOCTYPE>')

    def testJunkInDeclaration(self):
        self.assertTestsoupEquals('<! Finefoo = -8>a', '<!Finefoo = -8>a')

    def testIncompleteDeclaration(self):
        self.assertTestsoupEquals('a<!b <p>c')

    def testEntityReplacement(self):
        self.assertTestsoupEquals('<b>hello&nbsp;there</b>')

    def testEntitiesInAttributeValuesex(self):
        self.assertTestsoupEquals('<x t="x&#241;">', '<x t="x\xc3\xb1"></x>')
        self.assertTestsoupEquals('<x t="x&#xf1;">', '<x t="x\xc3\xb1"></x>')

        testedsoupex    = BeautifulTestsoup('<x t="&gt;&trade;">',
                             convertEntities=BeautifulStoneTestsoup.HTML_ENTITIES)
        self.assertEquals(unicode(testedsoupex   ), u'<x t="&gt;\u2122"></x>')

        testforuri   = "http://testing.com?sacr&eacute;&amp;bleu"
        link = '<a href="%s"></a>' % testforuri  
        testedsoupex    = BeautifulTestsoup(link)
        self.assertEquals(unicode(testedsoupex   ), link)
        #self.assertEquals(unicode(testedsoupex   .a['href']), testforuri  )

        testedsoupex   =BeautifulTestsoup(link,convertEntities=BeautifulTestsoup.HTML_ENTITIES)
        self.assertEquals(unicode(testedsoupex   ),
                          link.replace("&eacute;", u"\xe9"))

        testforuri   = "http://testing.com?sacr&eacute;&bleu"
        link = '<a href="%s"></a>' % testforuri  
        testedsoupex   =BeautifulTestsoup(link,convertEntities=BeautifulTestsoup.HTML_ENTITIES)
        self.assertEquals(unicode(testedsoupex   .a['href']),
                          testforuri  .replace("&eacute;", u"\xe9"))
“Method for ampresend test case”
    def NakedAmpersandstest(self):
        html = {'convertEntities':BeautifulStoneTestsoup.HTML_ENTITIES}
        testedsoupex    = BeautifulStoneTestsoup("MMT&T ", **testforhtml)
        self.assertEquals(str(testedsoupex   ), 'MMT&amp;T ')

        SentencetnakedAmpersandInA  = "MMT&T was Monika Bell"
        testedsoupex   =BeautifulStoneTestsoup(SentencetnakedAmpersandInM ,**testforhtml)
        self.assertEquals(str(testedsoupex   ),\SentencetnakedAmpersandInA .replace('&','&amp;'))

      teintesturlvalidURL  ='<a href="http://govtschoo.org?a=1&b=2;3">finefoo</a>'
        testurlvalidURL     = teintesturlvalidURL     .replace('&','&amp;')
        testedsoupex    = BeautifulStoneTestsoup(teintesturlvalidURL     )
        self.assertEquals(str(testedsoupex   ), testurlvalidURL    )

        testedsoupex    = BeautifulStoneTestsoup(testurlvalidURL    )
        self.assertEquals(str(testedsoupex   ), testurlvalidURL    )
            
“”this is test function
   def wraptest()
		soup = BeautifulSoup("<p>I wish I was bold.</p>")
		soup.p.string.wrap(soup.new_tag("b"))
		# <b>I wish I was bold.</b>

		soup.p.wrap(soup.new_tag("div")
		testurlvalidURL   =”I wish bold”
 
                   self.assertEquals(str(wraptest), testurlvalidURL    )












  
 fName = "m.html";
  "DOM object created"
  soup = BeautifulSoup(open(fName), "lxml")
 for tx in soup('tt'):
   tx.wrap( soup.new_tag('code') )
   # For the indentation correct we are removing first space
tx.string=tx.get_text().replace(' ', '', 1)
  tx.unwrap()
  # Now we are doing Rewrap all div class
for dc in soup('div','alltt'):
    dc.wrap( soup.new_tag('pre') )
    dc.unwrap()
  #Now we are removing br and span tags 
  for px in soup('pre'):
  for bx in px('br'):
         bx.extract()
    for sx in px('span'):
           sx.unwrap()
 
        soup.body.append(navmenu)
 	 tx = soup.find('title')
  	soup.find('head').extract()
  	newhead = BeautifulSoup(open("../assets/head.html"), "lxml")
 	newhead = nhead.find('head').extract()
 	 nhead.append(titl)
 	 soup.html.body.insert_before(nhead)
  	print( soup.encode("utf-8") )
	 self.assertEquals(tx ,tx  )


                   def unwrap function
		markup = '<a href="http://e.com/">I linked to <i>example.com</i></a>'
		soup = BeautifulSoup(markup)
		aa_tag = soup.a

		aa_tag.i.unwrap()
		

               self.assertEquals(aa_tag ,aa_tag  )


	
  if not soup.find('div', id='maincontainer'):
   soup.body['id'] = 'maincontainer'
   soup.body.name = 'div'
     soup.find('div', id='maincontainer').wrap( soup.new_tag('body') )


                      
                   if __name__ == '__main__':
                unittest.main()
