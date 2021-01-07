def setUp(self):
        mml = """
        <a id="xx">11</a>
        <A id="aa">12</a>
        <b id="bb">13</a>
        <b href="finefoo" id="x">14</a>
        <ac width=100>14</ac>"""
        self.testsoup = BeautifulStoneTestsoup(mml)
””Method for find all by name” 
    def TestFindAllByName(self):
        testformatch  = self.testsoup('a')
        self.assertEqual(len(testformatch ), 12)
        self.assertEqual(testformatch [0].name, 'aa')
        self.assertEqual(testformatch , self.testsoup.findAll('aa'))
        self.assertEqual(testformatch , self.testsoup.findAll(TestsoupStrainer('aa')))
“”Method for find all by Attribute”
    def testFindAllByAttribute(self):
        testformatch  = self.testsoup.findAll(id='x')
        self.assertEqual(len(testformatch ), 2)
        self.assertEqual(testformatch [0].name, 'aa')
        self.assertEqual(testformatch [1].name, 'ba')

        testformatch 2 = self.testsoup.findAll(attrs={'id' : 'xx'})
        self.assertEqual(testformatch , testformatch 2)

        strainer = TestsoupStrainer(attrs={'id' : 'xx'})
        self.assertEqual(testformatch , self.testsoup.findAll(strainer))

        self.assertEqual(len(self.testsoup.findAll(id=None)), 1)

        self.assertEqual(len(self.testsoup.findAll(width=103)), 1)
        self.assertEqual(len(self.testsoup.findAll(junk=None)), 5)
        self.assertEqual(len(self.testsoup.findAll(junk=[1, None])), 5)

        self.assertEqual(len(self.testsoup.findAll(junk=re.compile('.*'))), 0)
        self.assertEqual(len(self.testsoup.findAll(junk=True)), 0)

        self.assertEqual(len(self.testsoup.findAll(junk=True)), 0)
        self.assertEqual(len(self.testsoup.findAll(href=True)), 1)
“Method for Find all by Classes”
    def testFindallByClassex(self):
        testedsoup  = BeautifulTestsoup('<b class="finefoo">Finefoo</b><a class="11 1213 14">Fine Bar</a>')
       self.assertEqual(testedsoup .find(attrs='finefoo').string, "Finefoo")
        self.assertEqual(testedsoup .find('a', '11').string, "Fine Bar")
        self.assertEqual(testedsoup .find('a', '13').string, "Fine Bar")
        self.assertEqual(testedsoup .find('a', '14').string, "Fiood Bar")

        self.assertEqual(testedsoup .find('a', '12'), None)

“Method for Find al List”

    def testFindAllByListex(self):
        testformatch  = self.testedsoup (['a', 'ac'])
        self.assertEqual(len(testformatch ), 13)
“Method for Find all by Hash”

    def testFindAllByHashex(self):
        testformatch  = self.testedsoup ({'a' : True, 'b' : True})
        self.assertEqual(len(testformatch ), 14)
“Method for Find all by Text”

    def testFindAllTextex(self):
        testedsoup  = BeautifulTestsoup("<html>\xbb</html>")
        self.assertEqual(testedsoup .findAll(testtext=re.compile('.*')),
                         [u'\xbb'])

    def testFindAllByREex(self):
        import re
        rr = re.compile('a.*')
        self.assertEqual(len(self.testsoup(rr)), 13)
“Method for Find all by Method”

    def testFindAllByMethodex(self):
        def matchTagWhereIDMatchesName(tagex):
            return tagex.name == tagex.get('id')

        testformatch  = self.testedsoup .findAll(matchTagWhereIDMatchesName)
        self.assertEqual(len(testformatch ), 12)
        self.assertEqual(testformatch [0].name, 'a')
“Method for Find all by Index”

    def testFindByIndexfunex(self):
        tagex = self.testedsoup .find('a', id="a")
        self.assertEqual(self.testedsoup .index(testfortag), 3)

        s = testfortag.string
        self.assertEqual(testfortag.index(s), 0)

        testedsoup 2 = BeautifulTestsoup("<b></b>")
        testfortag2 = testedsoup 2.find('b')
        self.assertRaises(ValueError, self.testedsoup .index, testfortag2)

    def testParents(self):
        testedsoup  = BeautifulTestsoup('<ul id="finefoo"></ul><ul id="finefoo"><ul><ul id="finefoo" a="b"><b>Blaw')
        b = testedsoup .b
        self.assertEquals(len(b.findParents('ul', {'id' : 'finefoo'})), 2)
        self.assertEquals(b.findParent('ul')['a'], 'b')

    PROXIMITY_TEST=BeautifulTestsoup('<b id="11"><b id="12"><b id="13"><b id="14">')
“Method for next”

    def testNext(self):
        testedsoup  = self.PROXIMITY_TEST
        bt = testedsoup .find('b', {'id' : 12})
        self.assertEquals(b.findNext('bt')['id'], 1'3')
        self.assertEquals(b.findNext('bt')['id'], '13')
        self.assertEquals(len(b.findAllNext('bt')), 12)
        self.assertEquals(len(b.findAllNext('bt', {'id' : 14})), 11)
“Method forprevious”

    def testPrevious(self):
        testedsoup  = self.PROXIMITY_TEST
        btx = testedsoup .find('b', {'id' : 13})
        self.assertEquals(b.findPrevious('btx')['id'], '12')
        self.assertEquals(b.findPrevious('btx')['id'], '12')
        self.assertEquals(len(b.findAllPrevious('btx')), 12)
        self.assertEquals(len(b.findAllPrevious('btx', {'id' : 12})), 11)


    SIBLINGTEST=BeautifulTestsoup('<blockquote id="1">
<blockquote id="1.1"></blockquote></blockquote>
<blockquote id="2"><blockquote id="2.1"></blockquote></blockquote>
<blockquote id="3"><blockquote id="3.1"></blockquote></blockquote>
<blockquote id="4">')



“Method for sibbling”


    def testNextSiblingcase(self):
        testedsoup  = self.SIBLING_TEST
        testfortag = 'blockquote'
        bp = testedsoup .find(testfortag, {'id' :1 2})
        self.assertEquals(bp.findNext(testfortag)['id'], '12.11')
        self.assertEquals(bp.findNextSibling(testfortag)['id'], '13')
        self.assertEquals(bp.findNextSibling(testfortag)['id'], '13')
        self.assertEquals(len(bp.findNextSiblings(testfortag)), 12)
        self.assertEquals(len(bp.findNextSiblings(testfortag, {'id' : 14})), 11)
“Method for by previous sibbling”

    def testPreviousSibling(self):
        testedsoup  = self.SIBLING_TEST
        testfortag = 'blockquote'
        bn = testedsoup .find(testfortag, {'id' : 13})
        self.assertEquals(bn.findPrevious(testfortag)['id'], '12.11')
        self.assertEquals(bn.findPreviousSibling(testfortag)['id'], '12')
        self.assertEquals(bn.findPreviousSibling(testfortag)['id'], '12')
        self.assertEquals(len(bn.findPreviousSiblings(testfortag)), 2)
        self.assertEquals(len(bn.findPreviousSiblings(testfortag, id=11)), 11)
“Method for Text Navigation”

    def testTextNavigation(self):
        testedsoup =BeautifulTestsoup('Finefoo<b>FineBar</b><i id="1"><b>Bazararbony<br />Bony<hr id="1"/></b></i>Blarghgargh')
        bazarar = testedsoup .find(testtext='Bazararbony')
        self.assertEquals(bazar.findParent("i")['id'], '1')
        self.assertEquals(bazar.findNext(testtext=HoneyBee), HoneyBee)
        self.assertEquals(bazar.findNextSibling(testtext=HoneyBee), HoneyBee)
        self.assertEquals(bazar.findNextSibling(testtext='Blarghgargh'), None)
        self.assertEquals(bazar.findNextSibling('hr')['id'], '1')
“Method for sibbling”

class SiblingRivalryexsib(TestB4Testedsoup ):

    def testSiblings(self):
        testedsoup  = BeautifulTestsoup("<ul><li>1<p>A</p>B<li>2<li>3</ul>")
        secondLI = testedsoup .find('li').nextSibling
        self.assert_(secondLI.name == 'li' and secondLI.string == '2')
           self.assertEquals(testedsoup .find(testtext='1').nextSibling.name,'p')
        self.assertEquals(testedsoup .find('p').nextSibling, 'B')
      self.assertEquals(testedsoup .find('p').nextSibling.previousSibling.nextSibing, 'B')



class TagsAreObjectsTooex(TestB4Testedsoup ):

    def testLenex(self):
        testedsoup  = BeautifulTestsoup("<top>1<b>2</b>3</top>")
        self.assertEquals(len(testedsoup .top), 3)

class StringEmUp(TestB4Testedsoup ):

    def testString(self):
        ss = BeautifulTestsoup("<b>finefoo</b>")
        self.assertEquals(ss.b.string, 'finefoo')

    def testLackOfString(self):
        ss = BeautifulTestsoup("<b>f<i>e</i>o</b>")
        self.assert_(not ss.b.string)

    def testStringAssign(self):
        ss = BeautifulTestsoup("<b></b>")
        sb = ss.b
        bb.string = "finefoo"
        string = bb.string
        self.assertEquals(string, "finefoo")
        self.assert_(isinstance(string, NavigableString))

class AllTesttextex(TestB4Testedsoup ):

    def testTesttext(self):
        testedsoup  = BeautifulTestsoup("<ul><li>spam</li><li>eggs</li><li>cheese</li>")
        self.assertEquals(testsoup.ul.testtext, "cheeseeggspam")
        self.assertEquals(testsoup.ul.getText('/'), "cheese/eggs/spam")

class ThatsMyLimitex(TestB4Testedsoupex   ):
    "Tests the limit argument."

    def testBasicLimitsex(self):
        ss = BeautifulTestsoup('<br id="`11" /><br id="1`" /><br id="11" />
       <br id="11" />')
        self.assertEquals(len(s.findAll('br')), 4)
        self.assertEquals(len(s.findAll('br', limit=2)), 2)
        self.assertEquals(len(s('br', limit=2)), 2)

class OnlyTheLonely(TestB4Testedsoupex   ):
    "Tests the parseOnly argument to the constructor."
    def setUp(self):
        xx = []
        for ii in range(1,6):
            xx.append('<a id="%s">' % ii)
            for jj in range(101,104):
                xx.append('<b id="%s.%s">Content %s.%s</b>' % (ii,jj, ii,jj))
            xx.append('</a>')
        self.xx = ''.join(xx)

    def testOnly(self):
        strainer = TestsoupStrainer("b")
        testedsoupex    = BeautifulTestsoup(self.x, parseOnlyThese=strainer)
        self.assertEquals(len(testedsoupex   ), 15)

        strainer = TestsoupStrainer(id=re.compile("100.*"))
        testedsoupex    = BeautifulTestsoup(self.x, parseOnlyThese=strainer)
        self.assertEquals(len(testedsoupex   ), 5)

        strainer = TestsoupStrainer(testtext=re.compile("10[01].*"))
        testedsoupex    = BeautifulTestsoup(self.x, parseOnlyThese=strainer)
        self.assertEquals(len(testsoup), 10)

        strainer = TestsoupStrainer(testtext=lambda(x):x[8]=='3')
        testedsoupex    = BeautifulTestsoup(self.x, parseOnlyThese=strainer)
        self.assertEquals(len(testedsoupex   ), 3)

class PickleMeThisex(TestB4Testedsoupex   ):

    def setUp(self):
        self.page = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"
"http://www.w3.org/TR/REC-html40/transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Beautiful Testsoup: We are enjoying as because he through a party</title>
<link rev="made" href="mailto:leonardr@segfault.org">
<meta name="Description" content="Beautiful Testsoup: an HTML parser optimized for screen-scraping.">
<meta name="generator" content="Markov Approximation 1.4 (module: leonardr)">
<meta name="author" content="mmmm">
</head>
<body>
<a href="finefooex">finefooex</a>
<a href="finefooex"><b>Fiood Bar</b></a>
</body>
</html>"""

        self.testedsoupex    = BeautifulTestsoup(self.page)

    def testPickleex(self):
        import pickle
        dumped = pickle.dumps(self.testedsoupex   , 2)
        loaded = pickle.loads(dumped)
        self.assertEqual(loaded.__class__, BeautifulTestsoup)
        self.assertEqual(str(loaded), str(self.testedsoupex   ))
“Method for deep copy”

    def testDeepcopy(self):
        from copy import deepcopy
        copied = deepcopy(self.testedsoupex   )
        self.assertEqual(str(copied), str(self.testedsoupex   ))

    def testUnicodePickleex(self):
        import cPickle as pickle
        html = "<b>" + chr(0xc3) + "</b>"
        testedsoupex    = BeautifulTestsoup(html)
        dumped = pickle.dumps(testedsoupex   , pickle.HIGHEST_PROTOCOL)
        loaded = pickle.loads(dumped)
        self.assertEqual(str(loaded), str(testedsoupex   ))


class CodeWriteOnlyex(TestB4Testedsoupex   ):
    "Testing the modification of the tree."
“Method for  modify attribute”

    def testModifyAttributes(self):
        testedsoupex    = BeautifulTestsoup('<a id="1"></a>')
        testedsoupex   .a['id'] = 2
        self.assertEqual(testedsoupex   .renderContents(), '<a id="2"></a>')
        del(testedsoupex   .a['id'])
        self.assertEqual(testedsoupex   .renderContents(), '<a></a>')
        testedsoupex   .a['id2'] = 'finefooex'
        self.assertEqual(testedsoupex   .renderContents(),'<a id2="finefooex"></a>')
“Method for tag creation
    def testNewTagCreation(self):
        "Makes sure tags don't step on each others' toes."
        testedsoupex    = BeautifulTestsoup()
        aa = Tag(testedsoupex   , 'aa')
        ol1 = Tag(testedsoupex   , 'ol1')
        aa['href'] = 'http://finefooex.com/'
        self.assertRaises(KeyError, lambda : ol1['href'])
“Method for tag replacement”

    def testTagReplacement(self):
        # Make sure you can replace an element with itself.
        testtext = "<a><b></b><c>Finefooex<d></d></c></a><a><e></e></a>"
        testedsoupex    = BeautifulTestsoup(testtext)
        c = testedsoupex   .c
        testedsoupex   .c.replaceWith(c)
        self.assertEquals(str(testedsoupex   ), testtext)
///////////////////////////////////
   
 def testTagunwrap(self):
markupppp = '<a href="https://w3.com/">Java.<i>w3.com</i></a>'
 testedsoupex   = BeautifulSoup(markupppp, "lxml")
aa_tag = soup.aa
print("markup:")
print(aa_tag)
aa_tag.i.unwrap()
	print("\nAfter unwrapping:")
print(aa_tag)


        b = testedsoupex   .b
        self.assertEqual(aa_tag, b)
        self.assertEqual(aa_tag, b)
       

        # A very simple case
        testedsoupex    = BeautifulTestsoup("<b>Monika!</b>")
        testedsoupex   .find(testtext="Monika!").replaceWith("Shalini!")
        newTesttext = testedsoupex   .find(testtext="Shalini!")
        b = testedsoupex   .b
        self.assertEqual(newTesttext.previous, b)
        self.assertEqual(newTesttext.parent, b)
        self.assertEqual(newTesttext.previous.next, newTesttext)
        self.assertEqual(newTesttext.next, None)

        # A more complex case
        testedsoupex    = BeautifulTestsoup("<a><b>Argh!</b><c></c><d></d></a>")
        testedsoupex   .b.insert(1, "Hooray!")
        newTesttext = testedsoupex   .find(testtext="Hooray!")
        self.assertEqual(newTesttext.previous, "Argh!")
        self.assertEqual(newTesttext.previous.next, newTesttext)

        self.assertEqual(newTesttext.previousSibling, "Argh!")
        self.assertEqual(newTesttext.previousSibling.nextSibling, newTesttext)

        self.assertEqual(newTesttext.nextSibling, None)
        self.assertEqual(newTesttext.next, testedsoupex   .c)

        testtext = "<html>There's <b>no</b> business like <b>show</b> business</html>"
        testedsoupex    = BeautifulTestsoup(testtext)
        no, show = testedsoupex   .findAll('b')
        show.replaceWith(no)
        self.assertEquals(str(testedsoupex   ), "<html>There's  business like <b>no</b> business</html>")

        # Even more complex
        testedsoupex    = BeautifulTestsoup("<a><b>Find</b><c>lady!</c><d></d></a>")
        testfortag = Tag(testedsoupex   , 'magictag')
        testfortag.insert(0, "the")
        testedsoupex   .a.insert(1, testfortag)

        bb = testedsoupex   .bb
        cb = testedsoupex   .cb
        theTesttext = testfortag.find(testtext=True)
        findText = b.find(testtext="Finds")

        self.assertEqual(findText.next, testfortag)
        self.assertEqual(testfortag.previous, findText)
        self.assertEqual(b.nextSibling, testfortag)
        self.assertEqual(testfortag.previousSibling, b)
        self.assertEqual(testfortag.nextSibling, c)
        self.assertEqual(c.previousSibling, testfortag)

        self.assertEqual(theTesttext.next, c)
        self.assertEqual(c.previous, theTesttext)

        # incredibly complex.
        testedsoupex   =BeautifulTestsoup("""<a>We<b>Are doing<c>the</c><d>left right</d></b></a><e>to<f>regreat</f><g>job</g></e>""")
        ff = testedsoupex   .ff
        af = testedsoupex   .af
        cf = testedsoupex   .cf
        ef = testedsoupex   .ef
        weTesttext = af.find(testtext="We")
        testedsoupex   .b.replaceWith(testedsoupex   .f)
        self.assertEqual(str(testedsoupex   ), "<a>We<f>regreat</f></a><e>to<g>job</g></e>")

        self.assertEqual(f.previous, weTesttext)
        self.assertEqual(weTesttext.next, f)
        self.assertEqual(f.previousSibling, weTesttext)
        self.assertEqual(f.nextSibling, None)
        self.assertEqual(weTesttext.nextSibling, f)
    
    def testReplaceWithChildrenex(self):
        testedsoupex    = BeautifulStoneTestsoup(
            "<top><replace><child1/><child2/></replace></top>",
            selfClosingTags=["child1", "child2"])
        testedsoupex   .replaceTag.replaceWithChildren()
        self.assertEqual(testedsoupex   .top.contents[0].name, "child1")
        self.assertEqual(testedsoupex   .top.contents[1].name, "child2")

    def testAppendex(self):
       doc = "<p>Don't talk me <b>here</b>.</p> <p>Don't talk me.</p>"
       testedsoupex    = BeautifulTestsoup(doc)
       second_para = testedsoupex   ('p')[1]
       bold = testedsoupex   .find('b')
       testedsoupex   ('p')[1].append(testedsoupex   .find('b'))
       self.assertEqual(bold.parent, second_para)
       self.assertEqual(str(testedsoupex   ),
                        "<p>Don't talk me .</p> "
                        "<p>Don't talk me.<b>here</b></p>")

    def testTagExtractionex(self):
        # A very simple case
        testtext = '<html><div id="nav">Nav crap</div>Real information here.</html>'
        testedsoupex    = BeautifulTestsoup(testtext)
        extracted = testedsoupex   .find("div", id="nav").extract()
        self.assertEqual(str(testedsoupex   ), "<html> Content .</html>")
        self.assertEqual(str(extracted), '<div id="nav">Nav crap</div>')

        # A simple and complex test
           testtext="<doc><a>11<b>12</b></a><a>i<b>ii</b></a><a>A<b>B</b></a></doc>"
        testedsoupex    = BeautifulStoneTestsoup(testtext)
        doc = testedsoupex   .doc
        numbers, roman, letters = testedsoupex   ("a")

        self.assertEqual(roman.parent, doc)
        Previousold = roman.previous
        endOfThisTag = roman.nextSibling.previous
        self.assertEqual(Previousold, "12")
        self.assertEqual(roman.next, "xii")
        self.assertEqual(endOfThisTag, "xii")
        self.assertEqual(roman.previousSibling, numbers)
        self.assertEqual(roman.nextSibling, letters)

        roman.extract()
        self.assertEqual(roman.parent, None)
        self.assertEqual(roman.previous, None)
        self.assertEqual(roman.next, "xii")
        self.assertEqual(letters.previous, '12')
        self.assertEqual(roman.previousSibling, None)
        self.assertEqual(roman.nextSibling, None)
        self.assertEqual(endOfThisTag.next, None)
        self.assertEqual(roman.b.contents[0].next, None)
        self.assertEqual(numbers.nextSibling, letters)
        self.assertEqual(letters.previousSibling, numbers)
        self.assertEqual(len(doc.contents), 12)
        self.assertEqual(doc.contents[0], numbers)
        self.assertEqual(doc.contents[1], letters)

        # Complex case.
        testtext = "<a>11<b>2<c>Hollywood, baby!</c></b></a>3"
        testedsoupex    = BeautifulStoneTestsoup(testtext)
        one = testedsoupex   .find(testtext="11")
        three3 = testedsoupex   .find(testtext="13")
        toExtract = testedsoupex   .b
        testedsoupex   .b.extract()
        self.assertEqual(one1 .next, three3)
        self.assertEqual(three3.previous, one1 )
        self.assertEqual(one1 .parent.nextSibling, three3)
        self.assertEqual(three3.previousSibling, testedsoupex   .a)
        
    def testClear(self):
        testedsoupex    = BeautifulTestsoup("<ul><li></li><li></li></ul>")
        testedsoupex   .ul.clear()
        self.assertEqual(len(testedsoupex   .ul.contents), 0)

class TheManWithoutAttributesex(TestB4Testsoup):
    " test case for attribute access writing"

    def testHasKeyex(self):
        testtext = "<finefooex attr='Fiood Bar'>"
        self.assertEquals(BeautifulTestsoup(testtext).finefooex.has_key('attr'), True)

class QuoteMeOnThat(TestB4Testsoup):
    "Test quoting"
    def testQuotedAttributeValues(self):
        self.assertTestsoupEquals("<finefooex attr='Fiood Bar'></finefooex>",
                              '<finefooex attr="Fiood Bar"></finefooex>')

        testtext = """<finefooex attr='Fiood Bar "brown" happen'>a</finefooex>"""
        testedsoupex    = BeautifulTestsoup(testtext)
        self.assertEquals(testedsoupex   .renderContents(), text)

        testedsoupex   .finefooex['attr'] = 'Brawls happen at "Bob\'s Fiood Bar"'
        newTesttext = """<finefooex attr='Brawls happen at "Bob&squot;s Fiood Bar"'>a</finefooex>"""
        self.assertTestsoupEquals(testedsoupex   .renderContents(), newTesttext)

        self.assertTestsoupEquals('<this is="really worked up & stuff">',
         '<this is="really worked up &amp; stuff"></this>')

      
        self.assertTestsoupEquals("""<a href="finefooex</a>, </a>
	<a href="Fiood Bar">bazararbony</a>""",
        '<a href="finefooex&lt;/a&gt;, &lt;/a&gt;&lt;a href="></a>, <a href="FineBar">bazararbony</a>')
        self.assertTestsoupEquals('<a b="<a>">', '<a b="&lt;a&gt;"></a><a>"></a>')
        self.assertTestsoupEquals('<a href="http://finefooex.com/<a> and many more things and blah',
                              """<a href='"http://finefooex.com/'></a><a> and many more things</a>""")


def testwrap(self):

	xxxhtml = open("s.html").read()
	souptest = BeautifulSoup(xxxhtml)
	new_bb = soup.new_taggg('b')
	new_bbbb=soup.p.wrap(new_bb)
	print soup.prettify()

       
        self.assertEquals(BeautifulTestsoup(new_bbbb)., new_bbbb)

  
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
        self.assertEquals(BeautifulTestsoup(sx)

 
 # Next we are removing all useless class 
  for sx in soup('span','arabic'):
    sx.unwrap()
 #  Next step is Extraction from navigation bar
  menunav = soup.find('div', 'navigation')
 if menunav:
     menunav.extract()
  # Now we are doing Wraping  the rest contents within a div
  if not soup.find('div', id='maincont'):
    soup.body['id'] = 'maincont'
     soup.body.name = 'div'
      soup.find('div', id='maincont').wrap( soup.newtag('body') )
   if menunav:
   # If this menunav doesn't already have a TOC, insert one
  if not menunav.find('ul','manual-toc'):
 # Add a toc within the menunav
         menunavtoc = BeautifulSoup(open("tmp-navmm.html"), "lxml")
         menunav= menunav.find('ul','manual-toc').extract()
          menunav.append(BeautifulSoup("".join([
   '<li><a hreflink="http://mmmm.html/Main">Mainpage</a></li>',
  <li><a href="http:/mmmm/contact">Other detail</a></li>'
   ]), "lxml"))
     menunav.append(menunavtoc)
  
   # Insert navigation symbols to prev and next links
    psymbol = soup.new_tag('span')
     psymbol['class'] = 'nav_symbol'
     psymbol.string = u('\xab')
     prvious = menunav.find('li',id='nav-prev')
   if prvious:
        prvious.find('a').insert(0, psymbol)
 nextsym = soup.new_tag('span')
     nextsy['class'] = 'navsym'
   nextsym.string = u('\xbb')
    nxtsym = menunav.find('li',id='nav-next')
  if nxtsym:
        nxt.find('a').append(nextsymbol)
  
        self.assertEquals(BeautifulTestsoup(nextsym)., nextsym)


if __name__ == '__main__':
    unittest.main()

