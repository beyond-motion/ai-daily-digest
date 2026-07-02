# 每日摘要原始内容 | 2026-07-02

> 本文件由自动脚本抓取生成

---


=== https://daringfireball.net/2026/07/a_tale_of_two_modems ===
Title: A Tale of Two Modems

URL Source: https://daringfireball.net/2026/07/a_tale_of_two_modems

Markdown Content:
[Marko Zivkovic, reporting for AppleInsider](https://appleinsider.com/articles/26/06/30/iphone-18-pro-leaks-qualcomm-or-apple-c2-model-a20-details-camera-upgrades) regarding some of the data revealed by Tata Electronics’s massive data breach:

> For the U.S. variant of the iPhone 18 Pro, which will feature mmWave compatibility, Apple seemingly plans to use Qualcomm modem hardware. Multiple Qualcomm components, including the SDX80M, SDR875, QDM8771, QDM8720, PMK75, PMX75, and QET7100A, are referenced in a bill of materials related to the iPhone 18 Pro model Apple plans to sell in the United States.
> 
> 
> As for the iPhone 18 models which will be sold elsewhere, Tata documentation suggests these configurations will use Apple’s proprietary C2 modem. While this approach may sound unusual, there is at least one possible explanation.
> 
> 
> Apple’s current in-house modems, the C1 and the C1X, do not support 5G mmWave, and it looks as though the C2 will continue this trend. Until Apple develops a modem compatible with mmWave, it looks as though the company will offer mmWave support to iPhone 18 Pro users by using Qualcomm hardware.

This immediately raises the question of which modem is “better”, and I suspect the answer requires nuance. Apple’s C1 and C1X modems are, [by all accounts](https://birchtree.me/blog/battery-test-iphone-air-a-bunch-of/), noticeably more power efficient than Qualcomm’s. An iPhone with an Apple C-series modem should get longer batter life than an otherwise identical iPhone with a Qualcomm modem. The obvious advantage to the Qualcomm modems is support for 5G mmWave, the super high-speed 5G bands primarily offered by Verizon.

Personally, I don’t care about mmWave speeds. It literally makes no difference in my experience compared to regular 5G speeds. In fact, ever since WWDC a few weeks ago, I’ve had my iPhone 17 Pro set to use LTE instead of 5G. (Settings: Cellular: Cellular Data Options: Voice & Data.) I literally notice no difference in speed and I presume that battery life is improved. Battery life certainly isn’t worse. (I switched to LTE after a friend at WWDC suggested that LTE has better range/penetration in places like airports, especially when you’ve boarded a plane but haven’t taken off yet.)

Just now I used Ookla’s [Speedtest app](https://apps.apple.com/us/app/speedtest-by-ookla/id300704847) to test the difference here in my office. I got 80 Mbps down / 15 Mbps up on LTE; 320 Mbps down / 18 Mbps up on 5G. That’s on Verizon’s network (which does offer mmWave throughout center city Philly, but seemingly not here at my house), with my iPhone 17 Pro (which uses a Qualcomm modem). I tested again, minutes later, using an iPhone Air (which uses Apple’s C1X modem) and got 390 Mbps down / 21 Mbps up on 5G (and similar 80 Mbps down / 13 Mbps up on LTE).

So 5G is clearly faster than LTE here at home for me, using either iPhone model. But why should I care about that difference? Having a phone that can pull 320 Mbps down over cellular is like having a car that can go 320 MPH — an interesting technical feat, but of no practical value to me whatsoever. I never feel like I’m waiting for anything to load because I’m on LTE. LTE is fast enough, and regular 5G is more than fast enough. 5G mmWave is simply a waste of battery life as far as I’m concerned.

So Apple’s C-series modems win on battery life, and Qualcomm’s modems win for high-speed mmWave support. But Qualcomm’s speed edge is theoretical, not practical. Apple’s C1/C1X energy efficiency edge is very much practical. I’ve used both the 17 Pro and iPhone Air in a variety of places over the last year, and I’ve noticed no real difference in being able to get a decent signal in rural areas, either.

On the surface it sounds like a tradeoff — that Qualcomm’s modems consume more battery but deliver higher download speeds. But in practice that tradeoff only comes into play if you’re a Verizon user and happen to be within 50 meters or so of a mmWave-equipped cell tower, and that crazy high bandwidth doesn’t really make anything you do with your phone any faster than regular 5G (or LTE, I say). In reality I’d rather have an Apple C-series modem — I’d get better battery efficiency all the time, the same network performance almost all the time, and I don’t care at all about the rare times when I could get the crazy-high-speed mmWave bandwidth that Apple’s C1 and C1X modems don’t support (and perhaps still won’t support with the upcoming C2). Cellular download speed and reception is nearly a solved problem for my needs. Battery life is not.

So why wouldn’t Apple just use the C2 everywhere, including the U.S.? I suspect Apple is hoist not with their own, but with Verizon’s petard here. Faster-than-you-practically-need download speeds are a carrier bragging point. Longer battery life and plenty-fast-enough download speeds are an Apple bragging point. Verizon — and to a lesser extent, AT&T — spent a fortune building out mmWave networks. They don’t want to sell flagship phones that don’t support them. Apple’s flagship iPhones have supported those networks since 2020. Remember [how many times Tim Cook and Verizon’s CEO uttered “5G”](https://x.com/OnlyTechAE/status/1316529781777760256) at the Covid era iPhone 12 event? If Zivkovic’s analysis of this stolen data from Tata is correct, and Apple is going to use Qualcomm’s models _only_ in iPhone 18 Pro models sold in the U.S., I think the reason why is Verizon and AT&T bragging points, not any practical user benefit. And the result _may_ be that U.S. iPhone 18 Pro models get somewhat worse battery life than those in the rest of the world.

=== https://feed.tedium.co/link/15204/17371410/online-web-forums-retrospective ===
Title: What We Lost When We Quit Using Crappy Old Web Forums

URL Source: https://feed.tedium.co/link/15204/17371410/online-web-forums-retrospective

Markdown Content:
**Today in Tedium:** Recently, I passed 20,000 followers on Bluesky, which I didn’t really say anything about. Sure, I thought about it, but then I had decided to myself, what’s the point? Soon, there will be another mark I can point to and feel weird about. The thing about social media these days is that the good stuff all too often pulls you in, but at the end of the day, you end up feeling hollow. Perhaps it’s for this reason that, when I spotted a thread asking about what my favorite social network of all time was, my answer wasn’t Twitter or Bluesky or even Tumblr. It was, of all things, a forum for news designers that existed in the mid-2000s called Visual Editors. It barely worked, honestly: It had a chat option that was popular with designers waiting for their pages to get proofed late in the evening, but it would often go down with no warning. But from a community standpoint, it was spectacular. Why don’t many modern social networks feel like that? Today’s Tedium ponders the fate of the web forum. _— Ernie @ Tedium_

### 110k

**The number of newsgroups** that many modern Usenet providers, including [GigaNews](https://giganews.com/) and [SuperNews](https://www.supernews.com/usenet/), promote as being available on their services. The Usenet system, with roots in the late 1970s, was the first forum-like system many early internet users relied on, with the other primary option being email listservs. But by the late 1990s, the not-particularly-graphical Usenet was already falling out of favor.

![Image 1: post-it-notes.jpg](https://proxy.tedium.co/IzwEmfCClR4WnQfbzWRBfpocU_k=/1000x667/filters:quality(80)/uploads/post-it-notes.jpg)

For laypeople who have never used one: Forums function not unlike bulletin boards covered in rows of Post-It notes. ([Patrick Perkins/Unsplash](https://unsplash.com/photos/colorful-sticky-notes-pinned-to-board-ETRPjvb0KM0))

### Why the Web eventually moved in the direction of forums

**If you think about it,** the web forum was a terrible fit for the way the Web worked. We already technically had a tool that allowed people to communicate with one another in a forum setting in the early ’90s—[Usenet](https://tedium.co/2017/10/03/usenet-binaries-history/).

Or, at least, that’s what it seemed like. So I wondered, well, what did people think about the growth of web forums on Usenet? And that led me in the direction of a fascinating post from modern-day futurist Eric Hunting.

Posting on alt.hypertext in the thread “[Forums in the Web](https://usenetarchives.com/view.php?id=alt.hypertext&mid=PGh1bnRpbmcuMTExNzQ1ODMzMEJAdGlnZ2VyLmp2bmMubmV0Pg),” in April 1994, Hunting more or less predicted what web forums would become in just a couple of years:

> One of the things lacking in the environment of the Web is a means of using Web pages as a medium for conducting open discussions or forums as you have in USENET. The reason for this is probably that there is no means of packaging pages, along with all their associated graphics and multimedia data, like forum posts nor would it be practical to distribute such potentially huge amounts of data among forum servers as with USENET.

His post, which is a bit wordy, describes the concept of threads, URLs as organizing structures, and what might or might not work. Essentially, the addition of images and multimedia, a second-class citizen on a text-based forum like Usenet, would significantly reshape how people interacted on forums. One area where he was wrong, unfortunately, is a common one. He assumed that the lack of anonymity would lead people to behave a bit better online:

> It’s one thing to toss out a hundred lines of spontaneous vindictiveness to the faceless USENET server, another thing to have to maintain that mass of nastiness for a specific period of time on one’s own computer. A Web Forum post wouldn’t be a message on a paper airplane tossed to the aether. It would be a billboard in your own home.

Welp, not so much. But Hunting wouldn’t have to wait long to see an implementation of a web forum in the wild. In June 1994, CERN’s Ari Luotonen [developed](https://www.w3.org/WIT/) what is believed to be the first Web-based forum software, [WWW Interactive Talk](https://www.w3.org/WIT/) (WIT).

“[Bear] in mind that this was put together in a big hurry in a few days

 so forgive me if it doesn’t do yet all the things that it could do,” [Luotonen wrote](https://ksi.cpsc.ucalgary.ca/archives/WWW-TALK/www-talk-1994q2.messages/795.html).

The software did not live for long, and no longer appears on the W3C website—a surprise because much of its early work has more or less stayed online. Not this, though—though a little Internet Archive Wayback-foo eventually helped me find where the archive file was hiding.

In hopes of kicking back off a trend in W3C-generated forums, I uploaded the software to [GitHub](https://github.com/readtedium/WIT). And for kicks, I got it to run in a Docker container.

![Image 2: screenshot_2026-06-21_13-03-55.png](https://proxy.tedium.co/Wbr5tbPByC7rtlYFET8GKpkM-os=/849x547/filters:quality(80)/uploads/screenshot_2026-06-21_13-03-55.png)

If you can believe it, this forum actually works.

(Want to try it yourself? [I put it on the Web here](https://wit.tedium.co/). Watch out for falling spam.)

While the W3C was first, there are lots of examples of similar tools out there. For example, the [Collaborative Cork Board](https://jean-luc2.aei.mpg.de/Codes/CoCoBoard/index.html) (CoCoBoard) was developed at the University of Illinois’ National Center for Supercomputing Applications (NCSA), the same place that launched Mosaic into the world. That tool essentially turned email replies into forum threads.

It wasn’t long before this pie in the sky concept, once the experimental territory of early Web developers working in CGI and Perl, found interest with big businesses. These were promoted as one of many examples of [groupware](https://tedium.co/2024/04/13/groupware-workgroup-history/). Odds are, you probably did not get your first experience posting on a Web forum using an open-source tool, but a commercial one.

One of the first companies to successfully launch a web forum startup was Lundeen & Associates, which created the WebCrossing forum tool, which was announced in the fall of 1995. Within a year, a number of major publications, including the Minneapolis _Star-Tribune_, _The New York Times_, and _Salon_, had put the software to work—in the _Times_’ case, it was part of its 1996 election coverage. While later tools became better known, [WebCrossing](https://elliptics.com/webcrossing/) may be one of the few internet-native software tools to remain in active development for more than 30 years.

(A testament to its legacy: _Salon_ used the software as the anchor of its digital community for more than 15 years, only [shutting it down in 2011](https://www.salon.com/2011/05/13/tabletalk_closing_open2011/) out of concerns it wasn’t where the Web was going. With another 15 years of retrospect, can we argue that this was probably a bad move? Perhaps.)

But WebCrossing was far from alone. [The website Perlwatch](https://perlwatch.net/perl-applications/forums/#wikidforum) has a list of literally hundreds of different forum systems, some of which vary in levels of obscurity. The list, as far as I can tell, has not been updated in years, despite the site claiming otherwise. But it is an excellent historic document of what it was like looking for a bulletin board system in the late ’90s and early 2000s.

![Image 3: screenshot_2026-06-22_12-36-13.png](https://proxy.tedium.co/utfdy7lVsJ-AsJiHdWkSN0T39Iw=/943x801/filters:quality(80)/uploads/screenshot_2026-06-22_12-36-13.png)

The copyright notice for WWWBoard, the widely used forum-hosting software released by Matt’s Script Archive in the late ’90s.

But even with all this competition, the most dominant player in ’90s forum software benefited from being the free option. [Matt’s Script Archive](https://www.scriptarchive.com/), a collection of Perl-based website tools (including guestbooks and page counters), hit on something important with WWWboard.

That tool, a primitive forum technology that barely worked, nonetheless made threaded discussions accessible by normal people, even if it meant forums that extended well past the point of loadability and security issues that never get patched. (We wrote [a whole thing about it](https://tedium.co/2026/06/22/matts-script-archive-retrospective/) last week in case you want to dive in more.)

We quickly surpassed the limited capabilities of WWWBoard. But the forum itself would eventually get left in the dust, too.

![Image 4: Phpbb_3.0_prosilver.png](https://proxy.tedium.co/MRP3R-AjpBkJXTb4QZI8BreqiP4=/898x546/filters:quality(80)/uploads/Phpbb_3.0_prosilver.png)

An example of a phpBB forum, one of the most common types you’d see online in the early 2000s. (Wikimedia Commons)

### Five key examples of web forum software that are essential to internet history

1.   **[Ultimate Bulletin Board](https://www.ubbcentral.com/).** This software, later known as UBB and UBB.classic, found broad popularity on the internet thanks in large part to its low cost. It was a significant step up from WWWboard, in a good way. The software was originally developed around 1996 by Social Strata, which exists today under the name [CrowdStack](https://pro.crowdstack.com/). (That said, its history is a bit winding, so not every version may work the same.)
2.   **[Slash](https://sourceforge.net/projects/slashcode/).** Developed by Rob Malda in 1998 as a way to help manage the forums on his popular tech-news site [Slashdot](https://slashdot.org/), Slash proved supremely influential as a community management tool. (A big part of the reason? It came with really strong self-moderation features that were later copied by platforms like Hacker News, Digg, and Reddit.) While it’s not totally clear if Slashdot itself still uses Slash today (Malda, for one, left years ago), the site [SoylentNews](https://soylentnews.org/) is known to use a direct fork of it.
3.   **[vBulletin](https://www.vbulletin.com/).** This is one of the more recognizable forum platforms on the internet, in part because of its use on some very prominent forums. Notably, Something Awful’s [infamous forums](https://www.vice.com/en/article/fuck-you-and-die-an-oral-history-of-something-awful/) use vBulletin, but that’s only half the story there: The software was forked years ago, and has been heavily modified and customized by SA’s moderators and owners over the past two decades. At this point, it’s more theirs than vBulletin’s.
4.   **[phpBB](https://www.phpbb.com/).** While vBulletin, which came out around the same time as phpBB, is a commercial tool, phpBB has always been free and open source, and as a result, has found a massive community of people willing to write extensions for it. The similar [nodeBB](https://nodebb.org/) is a modernization of the phpBB approach and mostly works the same.
5.   **[Discourse](https://www.discourse.org/).** While it’s not the only tool of its kind, the decision by Jeff Atwood, Robin Ward, and Sam Saffron to build a new type of forum software was a big deal in 2014. After all, it was a medium in severe need of reinvention. (The move to a Ruby codebase, for example, was an important shift at a time when many forums still ran on PHP or Perl.) It can be seen as a continuation of Stack Exchange, a popular platform for programmer discussions that Atwood co-founded in 2008.

### 1985

**The year that The Whole Earth ‘Lectronic Link,** also known as [The Well](https://www.well.com/about-2/), first got its start. It is one of the longest continuously running online communities in digital culture, and unlike most bulletin boards or online services of its kind, it successfully made the jump to the Web. It remains active today as a paid private community. (The Well actually sponsored Tedium a million moons ago, which I realize is a cool thing to be able to say.)

![Image 5: BBCode_list.png](https://proxy.tedium.co/naIENNvunKcWYW7jJ2gNyDPqoMQ=/1109x991/filters:quality(80)/uploads/BBCode_list.png)

A list of some of BBCode’s layout options, as offered by the Something Awful Forums.

### Before there was Markdown, there was BBCode

One challenge that a lot of early forums had to navigate was the necessity of sanitizing the text that people posted in forums. People could post literally anything in a form, and it could break the site, encourage exploits, the whole bit.

(When you don’t sanitize, you run into issues like making it possible to [put CSS on MySpace pages](https://tedium.co/2020/07/14/social-media-customization-failings/).)

But on the other hand, you still wanted your websites to have at least _some_ style to them, in a controlled way, without a lot of extra junk. These days, a lot of platforms use Markdown to solve this problem, in part because of [its ubiquity](https://tedium.co/2026/02/17/markdown-growing-influence-cloudflare-ai/). But before that, people posting on forums needed alternative options that made room for fun if not for putting malware on your forum.

That led to the creation of BBCode in 1998, first starting with UBB, then spreading to other forum platforms like phpBB and vBulletin. (There is a BBCode dot org dedicated to this scripting language, but I refuse to link to it because it’s now a Web3 SEO play.) While it doesn’t get the modern level of attention Markdown does, it is both older and more capable than Markdown is, for better or worse.

A subset of HTML, it effectively replaced the `<` or `>` with `[` and `]`, and removed the ability to add a bunch of extra stuff that the HTML spec was capable of doing. Forum owners naturally appreciated this because it gave them a bit of control over what users could do on their platform. JavaScript might be off the table, but 300 point text? Suddenly possible. A library of common images? Absolutely, they were called image macros. And features that make the forum more usable? You bet.

This lingo would sometimes shape the community as a whole. Fans of Something Awful, for example, likely remember the forums had a number of image macros, most notably :10bux:, which displayed an image of a $10 bill, reflecting the forum’s infamous one-time entry fee. And on some forums, BBCode would end up getting used in experimental ways, helping to generate some early meme culture. In its own way, BBCode was what made forums more than just Usenet in HTML format.

The downside is that the security reasons were more pronounced in theory than in practice. [A 2005 blog post by developer Chris Shiflett](https://shiflett.org/articles/bbcode) argued that the security reason for BBCode was a lot weaker than it seemed:

> As regular readers of Security Corner know, input must always be filtered. When you’re allowing users to enter very complex data, creating a whitelist of acceptable characters can be very difficult. Because of this, many developers employ very weak filtering rules for such input and rely on the escaping performed by `htmlentities()` for protection.
> 
> 
> While `htmlentities()` can save you from poorly filtered data, relying on escaping alone is not ideal. Because an attacker can send any type of data, it’s equally unwise to rely on BBCode for protection—you can’t assume that the attackers will abide by your rules unless you enforce those rules in your programming logic.

But even if the security reasons didn’t matter so much, Shiflett conceded that it was good for users and may in some cases even be easier to remember than actual HTML. (Though on the other hand, one presumes BBCode did discourage some people from trying out forums entirely. Those were the people who eventually went to Facebook.)

A similar concept in content management systems associated with WordPress, the [shortcode](https://wordpress.com/support/wordpress-editor/blocks/shortcode-block/), became a popular technique for helping visually modify or organize content on a page. (Tedium uses shortcodes with Markdown.)

_More video games should be programmed with a little BBCode._

But what may be the most interesting legacy for BBCode in the modern day might not even be forums. The game development tool Godot [has adopted the scripting language](https://docs.godotengine.org/en/3.5/tutorials/ui/bbcode_in_richtextlabel.html) for writing formatted text within its node-driven interface. Which, given Godot’s [surge in popularity](https://godotengine.org/article/godot-growth-stats-2026/) over the past few years, likely means that a lot of modern games you enjoy might be secretly taking advantage of a tool developed for forum software built in Perl roughly 30 years ago.

Guess we can [indirectly blame Unity](https://www.pcworld.com/article/2069121/unity-has-done-the-impossible-united-gamers-and-developers-against-it.html) for helping give BBCode a second wind. What a story arc.

> ### “We’re shrinking the world. It used to be that just a few people saw your photo. Now many do. We helped people in Tunisia broadcast what was happening, and they could hear people around the world supporting them.”

**— Dick Costolo,** the former CEO of Twitter (in the pre-Elon days), discussing what made Twitter such a powerful tool. While this shrinking of our world might seem like a good thing (with the Arab Spring a go-to example at the time Costolo was leading the company), recent thinking has moved in a different direction. “There is something terribly wrong with social media,” psychologist Nigel Barber [argued in 2024](https://www.psychologytoday.com/us/blog/the-human-beast/202410/how-social-media-turn-societies-upside-down). “The problem is that they are run by an engagement algorithm that ignores the principles of successful communities.” The concept of content collapse likely also plays a role here. “The problem is not lack of context,” [cultural anthropologist Michael Wesch](https://www.academia.edu/2720713/YouTube_and_You_experiences_of_self_awareness_in_the_context_collapse_of_the_recording_webcam) wrote in 2009 about the then-new concept of YouTube. “It is context collapse: an infinite number of contexts collapsing upon one another into that single moment of recording.”

**Why did forums lose out to social media?** I think the short answer comes down to novelty. Much like Usenet a decade earlier, we were ready for something different, having seen the weaknesses of forums in the late 1990s and early 2000s. We were ready to let someone else handle the technology part.

Plus, there’s the issue of scale. In so many ways, having a forum run by someone in a community on shared hosting meant that you couldn’t have a community unless there was someone willing to take on that commitment. They were on the hook not just to pay for the hosting, but to spend a terrible night managing things when the server got full, hacked, or simply overheated because Slashdot linked one of your threads.

In many ways, the technical argument made it an easy target for Web 2.0. There’s a reason why Digg, Reddit, and StackOverflow are perhaps the best manifestations of that era of technology. They were purpose-built community platforms that modernized things just enough that people who were something a little better than we were getting from the thing that your friend built.

We tried the forum thing. We wanted something else. Not necessarily because it was better, though sure, maybe it was. But because it was different.

![Image 6: VisualEditors.png](https://proxy.tedium.co/mKnaJkFLijnhobk25CNZvUVhfg0=/818x781/filters:quality(80)/uploads/VisualEditors.png)

Visual Editors, the forum where I posted for way too many years before I discovered a thing called Twitter. Would I have been better off sticking with VizEds?

I want to pose a question: Is it possible that online users just have nonstop shiny object syndrome, and even if forums worked correctly and did the job, users would still move onto something else because we’re never happy? I think the argument is pretty strongly yes.

That said, I do think that as the internet matures into something that is more furniture in our lives, perhaps some of us will slow down. Maybe we’ll log into a forum and realize what we actually wanted out of our online experience was never the ability to reach everyone, but to reach the small number of people that think kind of like us. Maybe the “collisions” that modern social networks create just make things worse, even if it means we don’t get the occasional ego boost of Patton Oswalt replying to our tweet or whatever.

There was charm to all that barely-working PHP and Perl code that I think we’re still trying to recapture a quarter-century later.

--

Find this one an interesting read? [Share it with a pal](https://tedium.co/2026/07/01/online-web-forums-retrospective/)!

And we just added a bunch of new items to the [Tedium Shopping Network](https://shopping.tedium.co/). Maybe you might see something there you don’t need. Check it out.

=== https://www.dwarkesh.com/p/blog-prize-winners ===
Title: The Winning Essays for the Big Questions About AI

URL Source: https://www.dwarkesh.com/p/blog-prize-winners

Published Time: 2026-07-01T22:13:17+00:00

Markdown Content:
Two months ago, I posted some big questions about AI. We had 600 essays submitted for this contest. Below is a bit of information of the 3 winners, followed by all 3 full essay. Thanks to everyone who participated!

**First Place - Jassi Pannu**

[Jassi Pannu](https://jassipannu.substack.com/) is an Assistant Professor at Johns Hopkins University, where she focuses on biosecurity and pandemic preparedness. She serves on the board of Blueprint Biosecurity.

Jassi answered the question about what the OpenAI Foundation should do. She persuasively argues that we can live in a post-disease world, and gave very concrete and well thought out ideas about how to dedicate 10s of billions of dollars to that project.

**Second Place - Ege Erdil**

[Ege Erdil](https://x.com/EgeErdil2?lang=en) is a co-founder of [Mechanize](https://www.mechanize.work/), a startup building environments and evals for frontier coding agents. He was previously a researcher at Epoch AI.

Ege answered the question about what countries outside the AI supply chain should do to avoid increase their odds of not being totally sidestepped by transformative growth.

He argues that these countries should concentrate on enacting the kinds of policies that already work well in increasing growth and improving productivity. These strategies (strong property rights, low capital taxes, and an open regulatory regime) will be even more important in a world where enacting them can drive a much higher growth differential than is possible today.

What I love about Ege’s essay is that, in one sense, he’s giving very common-sense advice (as opposed to much more galaxy-brain schemes some other applicants proposed - one application suggested middle countries blackmail China and American by threatening to nuke their fabs and datacenters). But it’s actually this much more grounded and timeless advice that felt the most contrarian. And it’s also more likely to work.

**Third Place - Michael Li**

[Michael Li](https://x.com/michael_lwy) is a Master of Public Policy candidate at Harvard Kennedy School. He writes [Ceteris Paribus](https://michaellwy.substack.com/) — a blog at the intersection of emerging tech, econ and policy.

Michael wrote about how the labs will actually make money. His was selected for the unique analogy he drew between AI labs and Hong Kong’s Mass Transit Railway business model - even if your main product consumes crazy CapEx and doesn’t directly earn it back, maybe you can make up for it by buying out all the complementary assets. In the case of Hong Kong MTR, that would be the adjacent properties - I don’t know what it looks like for the AI labs, but it was a interesting analogy to think about.

I’d run the Foundation as a state-scale operation to end airborne transmission.

AI’s largest welfare upsides (curing diseases) and deadliest tail risks (engineered pandemics) both run through biology. By radically suppressing airborne pathogen transmission, we’d unlock >$1T in annual global GDP (through ending seasonal flu and the like, chronic diseases increasingly linked to viral infections, productivity losses, healthcare costs, etc.) and would take the possibility of catastrophic pandemics entirely off the table.

**The dual-payoff principle:** Most “make AI go well” interventions are insurance against bad outcomes, especially tail risks. My meta-level argument is that the best way of converting money into impact is to identify interventions that have the property of paying off big in both worlds: by producing step-changes in welfare in the everyday world as well as significantly reducing tail-risks in the emergency world. The bio resilience interventions I describe below are the best example of this.

**AI for biology is on the critical path to cures, but destabilizing capabilities will arise early**

Using AI to automate and scale every step in the biological research process, including managing the process itself (something I’ll call autonomous biological discovery), will bring humanity closer to a post-disease world. Over 4 billion years, life has been doing a random walk on an astronomically tiny subset of viable, connected, fitness-positive paths. Multi-component AI feedback loops (that include bio foundation models and systematic wet-lab experimentation at scale) for autonomous discovery will enable us to explore much more of possible biological design space. While we’re most interested in predicting and designing multicellular systems, it’s likely that the destabilizing capability of manipulating simpler pathogens will emerge first. The challenge this poses is that AI-enabled offense (seeding an outbreak) will be much easier than defense, which will remain constrained by physical-world deployment; I argue this advantages pre-positioned defensive technologies already embedded in our infrastructure.

**There’s a clear path to ending airborne transmission, using physical infrastructure.**

Regardless of what you think about the above, though, ending airborne transmission can be more than justified based on everyday benefits. Respiratory infections cause acute illness and productivity losses, but are increasingly linked to dementia, cardiovascular disease, and more; even “normal” childhood respiratory infections are being linked to long-term neurodevelopmental outcomes.

After evaluating many approaches, I’d argue ending airborne transmission is more achievable than most realize, through a specific, under-appreciated approach. I’m currently sitting in a building that provides me with pathogen-free water, keeps my food cold and pathogen-free, helps me heat my food to eliminate pathogens, and pipes away sewage. We have already embedded technologies all around us that enable a post-cholera, post-typhoid, post-dysentery world.

There is passive, pathogen-agnostic (works against any pathogen), physical infrastructure tech capable of making our buildings entirely free of respiratory pathogens, such as lamps that emit wavelengths safe for humans but are [deadly for bugs](https://blueprintbiosecurity.org/works/far-uvc/) (called far-UVC). Researchers have suspected these would work at scale for decades; the reasons we haven’t deployed them are primarily non-technological. Consider this analogical case.

We now live in a post-smallpox world. This is one of humanity’s greatest accomplishments. How long did it take for us to do this? Jenner demonstrated vaccination could prevent smallpox in 1796. 171 years later, in 1967, D.A. Henderson launched the campaign that would successfully eradicate smallpox. In that period of time, humanity discovered electromagnetism, thermodynamics, general relativity, and we were 2 years from landing on the moon. Eradication was accomplished within a mere 10 years (with limited tech advances). Delays in smallpox eradication, clean water, and pasteurized milk were not due to lack of tech advancement; they were primarily market and coordination failures exacerbated by lack of political will. This is why this problem is so philanthropy-shaped.

**4 steps to ending airborne transmission**

Total: ~$40-$60B over 10 years for physical infrastructure to end airborne transmission; the rest of OAIF’s stake remaining for other interventions meeting the dual-payoff principle. By year 10, every primary school and major transport hub in OECD countries operates with passive pathogen-reduction infrastructure as default. Seasonal flu mortality is reduced by 60%. The probability of a respiratory pathogen achieving pandemic-scale spread is reduced by an order of magnitude.

1.   Push-funding to resolve the target product profile ($5B, Years 1-3)→ Hire Jacob Swett, director of [Blueprint Biosecurity](https://blueprintbiosecurity.org/), to lead a DARPA-style program office focused on: a) pathogen inactivation data from human aerosols, b) computational modeling for deployment, c) safety studies beyond conventional UV effects, d) gold standard cluster-randomized trials powered to detect plausible effect sizes. By the end of year 3, deliver a validated TPP for far-UVC lamps and real-world efficacy data demonstrating >30% transmission reduction.

2.   AMCs to guarantee demand and pull private capital ($15B, Years 1-5)→ Create laddered purchase commitments for (a) 100K far-UVC fixtures that meet an interim TPP, (b) 1M for fixtures meeting the full TPP including safety and efficacy validation, (c) 10M commitment to retrofit specific buildings (see step 3). Modeled on Kremer’s pneumococcal vaccine AMC and Ransohoff/Frontier’s carbon removal commitments. By year 5, expectation is $30-50B in private capital mobilized, and supply chain capacity built to retrofit ~10% of global building stock.

3.   Large-scale deployments to generate evidence ($15-25B, Years 2-7)→ Years 2-4: Deploy in all hospitals and long-term care facilities in 50 largest metro areas globally. Years 3-6: Primary and secondary schools in the same metro areas. Years 2-7: Major airports and high-density workplaces. By year 7, substantial real-world evidence base.

4.   Political infrastructure and state handoff ($3-5B, Years 1-10)→ Smallpox eradication was a genuinely contingent historical event predicated on political will. Fund a memetic campaign à la the Rockefeller Foundation’s IHD yellow fever playbook which would transform respiratory transmission from “normal” to undesirable/unnecessary, and the training of a cadre of thousands that move into governments to build the political constituency and institutional infrastructure needed for global deployment and standards-setting. When pilot deployments demonstrate ≥40% reduction across 3 OECD countries, the Foundation transitions to catalyst rather than principal funder role, activating state procurement at orders-of-magnitude scale.

I think a good baseline which very few countries, in the AI supply chain or not, will beat is “do nothing and ignore populist pressures to take radical actions”.

This is because people are naturally technologically conservative, and they hate economic disruption that causes job losses. Full automation of human labor by AI would bring about rapid technological and economic progress that would result in all humans losing their jobs. So the default expectation should be that policymaking in an era of AI automation will be profoundly irrational and counterproductive.

Resisting this political pressure will be hard enough for even the most functional governments. Expecting more from governments with poor track records such as India and Nigeria is unreasonable.

**What does good policy in the AI era look like?**

Having given this basic but uninspiring answer, I’ll now flesh out what I actually think will be important for good policymaking in the era of AI automation, though in practice it’s unlikely to have much relevance for how policy decisions will be taken.

Today, the economic output of a country depends on its endowment of natural resources, on how much physical and human capital it has, and how efficiently it’s able to make use of these resources. The major shift with AI will be that human capital will drop out of this equation. If a country wants to do well in a world after full automation of labor; they need more natural resources, more capital, or more ability to make use of these inputs effectively, i.e. more total factor productivity.

While the capital elasticity of output will dominate any other factor of production, how much capital a country ends up with is itself endogenous. Capital moves across borders more easily than labor, and it will likely flow to the places where factors complementary to it – total factor productivity and natural resources – are abundant.

So I think the pillars of good policy in the AI era involve going in the following directions, to whatever extent possible:

*   Get out of the way of AI automation. Repeal or revise occupational licensing laws, liability laws, data protection laws, and intellectual property. Abolish price and wage controls. Dismantle cartels and unions of human workers who will try to protect themselves from AI competition. Apply safety and security standards consistently between humans and AIs, instead of discriminating in favor of humans. Make it much easier to start new businesses, as AIs will need organizational structures just as much as humans do in order to bring out their productive potential.

*   Provide political and legal stability. Investment will be anemic under instability, and if a country can stand out as an island of stability in what will likely be tumultuous decades for the world, it will attract enormous amounts of investment. The lowest bar is avoiding civil wars, revolutions or coups (not trivial for Nigeria to clear, since there was a serious military conspiracy to overthrow Tinubu as recently as September 2025); but this is not enough by itself. People must be confident that their investments will not be expropriated, and that the core operation of their businesses won’t suddenly be declared illegal.

*   Increase capital formation in your country. Reduce or eliminate taxes on capital gains and corporate income, don’t let important projects be held up by permitting, don’t hamper construction by requirements of “having to pay prevailing wages”. Remove exchange, interest rate, and capital controls.

*   If industries necessary for AI deployment are broken, urgently fix them. For example, Nigeria’s grid sucks and needs to be fixed before anything else can happen, and this is downstream of the entire economy’s price system being messed up by government restrictions. If this isn’t fixed, the country will never be able to accumulate the kind of capital it needs to be productive in an era of AI automation.

These recommendations feel extreme because humans instinctively like policies that favor labor over capital. This already causes problems in our world where capital’s output share is only around 30%, but it will likely become a critical obstacle in a world where labor has been made obsolete and capital’s output share is much higher.

If a country that’s currently in bad shape succeeds in doing these, they would attract a ridiculous amount of outside investment and be transformed in the decades in which AI automates the world economy. The fact that they had no previous AI labs or fab companies with trillion dollar valuations would be irrelevant, because those very companies would at that moment be in the process of automating their moat – their human capital and organizational knowledge – away.

**Will this happen?**

Probably not. As I’ve said, the relevant countries are far too dysfunctional for these radical reforms to be adopted, and the countries currently in the AI supply chain (e.g. the US and China) already perform well relative to other countries on the metrics I’ve listed.

However, there’s still some hope for countries outside the AI supply chain: the incumbents can screw up. This is not that implausible, because policy quality in the industrial era will not be that strongly correlated with policy quality in the AI era, just like how the best foraging economies in the world weren’t the best agrarian ones and the best agrarian economies weren’t the best industrial ones.

Concretely, the incumbents can outlaw AI automation in key industries, slow down datacenter buildouts, expropriate capital holders, impose strict safety standards for rolling out AI agents in critical industries like medicine and law, et cetera. There’s virtually no limit to the mistakes that they can make in the coming period of acute irrationality. If a mediocre country simply holds on and doesn’t make any big blunders, they will probably come out the other side of this in a much better relative position than they had been in at the start.

**A subway company solved AI’s business model**

There is an industry with the following economics: billions in upfront capital before earning a dollar. Core service priced near marginal cost. Enormous value created for users, almost none captured by the builder. Relentless pressure to keep investing in the next generation of infrastructure. I’m not talking about AI labs. I’m talking about Hong Kong’s Mass Transit Railway.

Many have reached for the railroads analogy when discussing the business of AI. Most conclude that the lesson is commercial viability requires state subsidy for a general purpose technology with public good properties.

I want to challenge that, because Hong Kong’s MTR actually solved the problem. It’s one of the only mass transit systems in the world that is commercially self-sustaining, publicly listed, paying dividends with no government operating subsidy.

**The financials are structurally identical**

MTR’s core rail service has never funded its own expansion. In [2018](https://www.mtr.com.hk/archive/corporate/en/investor/pre_blackout_202407.pdf), its best pre-covid year, transport operations earned HK$2.0 billion in EBIT. [Estimated capital expenditure for 2024–2026 is HK$87.9 billion](https://www.mtr.com.hk/archive/corporate/en/investor/pre_blackout_202407.pdf), nearly all rail-related. Three years of peak rail earnings would cover 8% of that. The rail has never paid for itself through fares. It was never designed to.

MTR fares are kept affordable through a [government fare adjustment mechanism](https://www.mtr.com.hk/sustainability/en/financial-sustainability.html). You can’t price transit to recover full construction costs because it would be unaffordable and defeat the purpose. Each rail line can maybe cover its operating costs, but fare revenue never stretches to fund the next line. AI API pricing faces the same constraint from the other direction. Distillation and open source alternatives deflate API prices roughly [10x per year](https://epoch.ai/gradient-updates/can-ai-companies-become-profitable), and any lab that prices above marginal cost loses volume to rivals. Each model can be [operationally profitable](https://epoch.ai/gradient-updates/can-ai-companies-become-profitable) on inference, but the margin never stretches to fund the next training run.

The standard global solution is subsidy. London Underground requires billions in TfL grants. China’s national HSR carries a trillion dollars in debt with 94% of routes unprofitable. AI is on the same trajectory: CHIPS Act, Stargate, sovereign wealth fund investments, Pentagon contracts. The default endpoint is subsidy-dependent quasi-public infrastructure.

MTR found another way.

**Rail plus property**

When MTR was built in 1979, its designers understood that fares alone would never recover construction costs. So they structured the corporation around a different premise: the rail line would make surrounding land valuable. So own the land.

MTR develops residential towers, offices and shopping malls above and adjacent to its stations, capturing the value appreciation that its own infrastructure creates. Property profits cross-subsidize rail operations and fund the next line. Today MTR owns [13 shopping malls, manages 47 developments above its stations](https://en.wikipedia.org/wiki/MTR_Corporation), and property generates the [majority of actual profit](https://www.minichart.com.sg/2026/03/12/mtr-corporation-2025-annual-results-financial-performance-property-development-and-railway-expansion-updates/). Don’t try to capture value through the rail service itself. Own the assets that appreciate because of the rail service.

**The AI parallel**

“When do labs make money?” has the same structure as “when does rail pay for itself through fares?” It doesn’t, and that’s the wrong question.

A biotech startup uses a frontier model to screen drug compounds, shaving two years off a clinical trial. A logistics firm uses it to optimize routing, saving $40 million in fuel costs. A solo developer ships in a weekend what used to take a five person team three months. In each case the model provider captures a fraction of a percent through API fees. The provider can’t charge more, because four other labs and a dozen open source alternatives offer comparable capability. The surplus flows to the users and the broader economy. This is what general purpose technologies do. The steam engine, electricity and TCP/IP generated zero revenue for their creators.

MTR’s lesson: stop trying to make fares cover construction. Find the property.

**Four candidates, ranked by defensibility**

**Government-granted deployment rights come first.**A government grants a lab exclusive deployment access to national health records, tax systems or defense logistics. The lab accumulates domain data, integration depth and regulatory clearance that takes years to replicate. This is MTR’s own mechanism: development rights granted by the state, justified by natural monopoly properties.

**Accumulated RL reward data is second.** Billions of interaction signals that train the next model generation. Unlike weights (which depreciate via distillation), RL data is practically non-replicable and compounds across generations. It doesn’t convert to revenue directly, but it’s a land bank. Appreciating, undeveloped.

**Forward-deployed integration is third.** Instead of selling model access to a consulting firm that captures the productivity surplus, own the service delivery end to end. The way Palantir embeds engineers inside government agencies rather than licensing software. The lab doesn’t charge the law firm an API fee. The lab becomes the legal research service, priced against the outcome it delivers rather than the tokens it serves. Switching costs compound with accumulated domain data and institutional knowledge. This is MTR’s shopping mall: capture the foot traffic the rail creates rather than charging passengers more for the ride.

**Data trusteeship over national datasets is fourth.**Governments sit on enormous under-leveraged datasets (patient records, tax filings). A frontier lab designated as trustee gets exclusive access to train on and build products against this data. The scarcity is genuine, justified by the same logic as MTR’s land. You don’t want five competing labs accessing fifty million patient records any more than you want five developers building on the same plot. But this creates a public-private data monopoly and would require careful governance: clear boundaries on usage, benefits flowing back to the public, independent monitoring and real sanctions for misuse.

**The reframe**

The labs that survive won’t be the ones that make the API profitable. They’ll be the ones that identify their property above the station and build toward it now. The API is the rail. It will never be profitable enough. The money is in what appreciates around it.

The policy question follows: instead of subsidizing training runs, governments should design institutional mechanisms (deployment rights frameworks, data trusteeship structures, productivity measurement standards) that let labs capture the surplus their infrastructure creates.

There’s a final irony. The AI policy conversation is dominated by the US-China frame. American free market labs versus Chinese state-funded champions. The most relevant institutional model may be neither. It may be Hong Kong’s: a 45 year old public-private hybrid, commercially operated, self-financing through institutional design rather than ideology. The model that makes frontier AI sustainable might already exist. It just runs trains.

=== https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/ ===
Title: Apple ‘Hide My Email’ Vulnerability Reveals Peoples’ Real Email Addresses

URL Source: https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/

Published Time: 2026-07-01T10:00:57.000Z

Markdown Content:
Listen to the [404 Media Podcast](https://www.404media.co/the-404-media-podcast/)

[](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/)

###### Account

*   [Log in](https://www.404media.co/signin/)
*   [Subscribe](https://www.404media.co/signup/)

###### Navigation

*   [Home](https://www.404media.co/)

*   [About](https://www.404media.co/about/)
*   [RSS](https://www.404media.co/404-media-now-has-a-full-text-rss-feed/)
*   [Support/FAQ](https://www.404media.co/faq/)
*   [Podcast](https://www.404media.co/the-404-media-podcast/)
*   [FOIA Forum Archive](https://www.404media.co/foia-forum-archive/)
*   [Merch](https://404media.myshopify.com/)
*   [Advertise](https://www.404media.co/advertise-with-404-media/)
*   [Privacy](https://www.404media.co/privacy-policy/)
*   [Contact Us/Tips](https://www.404media.co/contact-us-tips/)

###### Follow us

[Twitter](https://x.com/404mediaco "Twitter")[Bluesky](https://bsky.app/profile/404media.co "Bluesky")[Mastodon](https://mastodon.social/@404mediaco "Mastodon")[Instagram](https://instagram.com/404mediaco "Instagram")[TikTok](https://tiktok.com/@404.media "TikTok")[Facebook](https://www.facebook.com/404mediaco "Facebook")[RSS](https://www.404media.co/rss "RSS")

[](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/ "Search")

[](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/ "Dark Theme")[](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/ "Light Theme")

[](https://www.404media.co/)

[Sign in](https://www.404media.co/signin/)[Subscribe](https://www.404media.co/signup/)

*   [About](https://www.404media.co/about/)
*   [RSS](https://www.404media.co/404-media-now-has-a-full-text-rss-feed/)
*   [Support/FAQ](https://www.404media.co/faq/)
*   [Podcast](https://www.404media.co/the-404-media-podcast/)
*   [FOIA Forum Archive](https://www.404media.co/foia-forum-archive/)
*   [Merch](https://404media.myshopify.com/)
*   [Advertise](https://www.404media.co/advertise-with-404-media/)
*   [Privacy](https://www.404media.co/privacy-policy/)
*   [Contact Us/Tips](https://www.404media.co/contact-us-tips/)

Advertisement

•

[Go ad free](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/#/portal/signup)

[![Image 1](https://static4.buysellads.net/uu/7/176474/1782935278-Cape_Logo_Black.png) Sponsored by Cape Cell service built from the ground up with privacy and security at its core. Switch to Cape](https://srv.buysellads.com/ads/click/x/GTND427YCVAIC237CTALYKQUFT7IC2J7C6ADLZ3JCAADC2QLCAAIKK3KC6YIC27ICTYDPKJECWADTKJICKYD45QJHEYI553LF6BIT23ECTNCYBZ52K?segment=placement:404media-leaderboard "Cape — America's Privacy-First Mobile Carrier")

[Privacy](https://www.404media.co/tag/privacy/ "Privacy")
# Apple ‘Hide My Email’ Vulnerability Reveals Peoples’ Real Email Addresses

[![Image 2: Joseph Cox](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w100/2023/08/404-joseph-01-1.jpg)Joseph Cox](https://www.404media.co/author/joseph-cox/ "Joseph Cox")

· Jul 1, 2026 at 6:00 AM 

”Hide My Email users deserve to know that it may be possible for attackers to discover their hidden email addresses,” the person who reported the issue said.

![Image 3: Apple ‘Hide My Email’ Vulnerability Reveals Peoples’ Real Email Addresses](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w2000/2026/06/laurenz-heymann-wAygsCk20h8-unsplash.jpg)

Photo by[Laurenz Heymann](https://unsplash.com/@lagommedia?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)on[Unsplash](https://unsplash.com/photos/apple-logo-on-glass-window-wAygsCk20h8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

[404 Media is an independent website whose work is written, reported, and owned by human journalists. Our intended audience is real people, not AI scrapers, bots, or a search algorithm. Become a paid subscriber here for access to all of our articles ad-free and bonus content.](https://www.404media.co/#/portal)

A vulnerability in Apple’s “Hide My Email” tool lets almost anyone discover a person’s real email address that is supposed to be hidden by the feature, and Apple has failed to fix it for more than a year, according to a security researcher and 404 Media’s own tests.

404 Media is not revealing the exact details of the vulnerability because it can still be exploited as of Monday, when 404 Media verified the issue with one of our own hidden email addresses.

## This post is for paid members only

Become a paid member for unlimited ad-free access to articles, bonus podcast content, and more.

[Subscribe](https://www.404media.co/membership/)

## Sign up for free access to this post

Free members get access to posts like this one along with an email round-up of our week's stories.

[Subscribe](https://www.404media.co/signup/)

Already have an account? [Sign in](https://www.404media.co/signin/)

###### More like this

[![Image 4: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/census-data-privacy-trump-policy-change-noise-infusion/ "The Trump Administration’s New Census Data Rules Are a Policy Disaster")

[The Trump Administration’s New Census Data Rules Are a Policy Disaster](https://www.404media.co/census-data-privacy-trump-policy-change-noise-infusion/ "The Trump Administration’s New Census Data Rules Are a Policy Disaster")

 The new policy, which forbids "noise infusion" as a technique for anonymizing data, will "handcuff" the Census Bureau and limit what information becomes public, data experts say. 

[![Image 5: Samantha Cole](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2023/08/404-sam-10--1-.jpg)Samantha Cole](https://www.404media.co/author/samantha-cole/ "Samantha Cole")

· Jun 24, 2026 

[![Image 6: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/madison-square-garden-made-dossier-on-activists-who-opposed-facial-recognition/ "Madison Square Garden Made Dossier on Activists Who Opposed Facial Recognition")

[Madison Square Garden Made Dossier on Activists Who Opposed Facial Recognition](https://www.404media.co/madison-square-garden-made-dossier-on-activists-who-opposed-facial-recognition/ "Madison Square Garden Made Dossier on Activists Who Opposed Facial Recognition")

 The document, titled “Facial Recognition Activists.docx,” includes specific activists’ comments about MSG's facial recognition program and tweets criticizing it. 

[![Image 7: Joseph Cox](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2023/08/404-joseph-01-1.jpg)Joseph Cox](https://www.404media.co/author/joseph-cox/ "Joseph Cox")

· Jun 23, 2026 

[![Image 8: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/ "FCC Wants to Kill Burner Phones By Forcing Telecoms to Get All Customers’ IDs")

[FCC Wants to Kill Burner Phones By Forcing Telecoms to Get All Customers’ IDs](https://www.404media.co/fcc-wants-to-kill-burner-phones-by-forcing-telecoms-to-get-all-customers-ids/ "FCC Wants to Kill Burner Phones By Forcing Telecoms to Get All Customers’ IDs")

 The FCC wants to legally force telecoms to collect new and renewing customers’ government issued identity number and physical address, impacting everyone from the privacy-conscious to domestic abuse survivors. “We never thought that would happen here.” 

[![Image 9: Joseph Cox](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2023/08/404-joseph-01-1.jpg)Joseph Cox](https://www.404media.co/author/joseph-cox/ "Joseph Cox")

· Jun 9, 2026 

[![Image 10: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/podcast-the-ai-tokenpocalypse-is-here/ "Podcast: The AI Tokenpocalypse Is Here")

[Podcast: The AI Tokenpocalypse Is Here](https://www.404media.co/podcast-the-ai-tokenpocalypse-is-here/ "Podcast: The AI Tokenpocalypse Is Here")

 How companies are burning through their AI tokens; and the fake AI-generated flowers all over Etsy, eBay, and Amazon. 

[![Image 11: Joseph Cox](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2023/08/404-joseph-01-1.jpg)Joseph Cox](https://www.404media.co/author/joseph-cox/ "Joseph Cox")

· Jul 1, 2026 

[![Image 12: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/untitled-28/ "Scientists Asked AI to Impersonate 112 Public Figures. What Happened Next Is a ‘Dire’ Warning")

[Scientists Asked AI to Impersonate 112 Public Figures. What Happened Next Is a ‘Dire’ Warning](https://www.404media.co/untitled-28/ "Scientists Asked AI to Impersonate 112 Public Figures. What Happened Next Is a ‘Dire’ Warning")

 Researchers discovered that people found AI impersonators to be more authentic, coherent, and relevant than the real politicians, raising alarm bells around the potential for public deception. 

[![Image 13: Becky Ferreira](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2024/09/7BaR_tNV_400x400-1.jpg)Becky Ferreira](https://www.404media.co/author/becky/ "Becky Ferreira")

· Jul 1, 2026 

[![Image 14: I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/assets/images/img-placeholder-md.jpg?v=25d884193e)](https://www.404media.co/meta-smart-glasses-starfire-kylie-jenner/ "I Have Thoughts About That Kylie Jenner Meta Glasses Ad")

[I Have Thoughts About That Kylie Jenner Meta Glasses Ad](https://www.404media.co/meta-smart-glasses-starfire-kylie-jenner/ "I Have Thoughts About That Kylie Jenner Meta Glasses Ad")

 Meta's new Starfire AI glasses, made in partnership with Kylie Jenner, are giving me the creeps. 

[![Image 15: Samantha Cole](https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/size/w30/2023/08/404-sam-10--1-.jpg)Samantha Cole](https://www.404media.co/author/samantha-cole/ "Samantha Cole")

· Jun 30, 2026 

Advertisement

•

[Go ad free](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/#/portal/signup)

Advertisement

•

[Go ad free](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/#/portal/signup)

•

[Hide](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/)

### Unparalleled access to hidden worlds both online and IRL.

 404 Media is an independent media company founded by technology journalists Jason Koebler, Emanuel Maiberg, Samantha Cole, and Joseph Cox. 

*   [About](https://www.404media.co/about/)
*   [RSS](https://www.404media.co/404-media-now-has-a-full-text-rss-feed/)
*   [Support/FAQ](https://www.404media.co/faq/)
*   [Podcast](https://www.404media.co/the-404-media-podcast/)
*   [FOIA Forum Archive](https://www.404media.co/foia-forum-archive/)
*   [Merch](https://404media.myshopify.com/)
*   [Advertise](https://www.404media.co/advertise-with-404-media/)
*   [Privacy](https://www.404media.co/privacy-policy/)
*   [Contact Us/Tips](https://www.404media.co/contact-us-tips/)

[Twitter](https://x.com/404mediaco "Twitter")[Bluesky](https://bsky.app/profile/404media.co "Bluesky")[Mastodon](https://mastodon.social/@404mediaco "Mastodon")[Instagram](https://instagram.com/404mediaco "Instagram")[TikTok](https://tiktok.com/@404.media "TikTok")[Facebook](https://www.facebook.com/404mediaco "Facebook")[RSS](https://www.404media.co/rss "RSS")

Join the newsletter to get the latest updates.

Success

 Great! Check your inbox and click the link to confirm your subscription 

©2026 404 Media. Published with[Ghost](https://ghost.org/). 

## Keep reading with your email. It's free

404 Media is made by humans, for humans. We don't want AI scraping our work, and we don't use AI to write our articles. Providing your email ensures that our audience is who we want—people like you.

Subscribe

- [x] [By signing up, you agree to receive emails from us.](https://www.404media.co/privacy-policy/) 

Great! Check your inbox and click the link.

Sorry, something went wrong. Please try again.

Already a member? [Sign in](https://www.404media.co/apple-hide-my-email-vulnerability-reveals-peoples-real-email-addresses/#/portal/signin)

![Image 16: CTA Image](https://www.404media.co/content/images/2023/08/favicon-3.svg)

=== https://pluralistic.net/2026/07/01/ontogeny/ ===
Title: Daily links from Cory Doctorow

URL Source: https://pluralistic.net/2026/07/01/ontogeny/

Markdown Content:
[![Image 1](https://i0.wp.com/craphound.com/images/01Jul2026.jpg?w=840&ssl=1)](https://pluralistic.net/2026/07/01/ontogeny/)

## Today's links

*   [Technocarcinization](https://pluralistic.net/2026/07/01/ontogeny/#recapitulates-phylogeny): Enshittification is the great leveler. 
*   [Hey look at this](https://pluralistic.net/2026/07/01/ontogeny/#linkdump): Delights to delectate. 
*   [Object permanence](https://pluralistic.net/2026/07/01/ontogeny/#retro): Grampa's backyard Disneyland; Elizabeth Warren on monopolies; Spotify v Apple (antitrust edn); Exxon lobbyist confesses; "When the Sparrow Falls." 
*   [Upcoming appearances](https://pluralistic.net/2026/07/01/ontogeny/#upcoming): London, Edinburgh, Sydney, Melbourne, Brighton, London, South Bend. 
*   [Recent appearances](https://pluralistic.net/2026/07/01/ontogeny/#recent): Where I've been. 
*   [Latest books](https://pluralistic.net/2026/07/01/ontogeny/#latest): You keep readin' em, I'll keep writin' 'em. 
*   [Upcoming books](https://pluralistic.net/2026/07/01/ontogeny/#upcoming-books): Like I said, I'll keep writin' 'em. 
*   [Colophon](https://pluralistic.net/2026/07/01/ontogeny/#bragsheet): All the rest. 

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 2: Two crabs dance with their claws entwined; one has the Google logo on its back, the other, the Apple logo. Their audience is a much larger crab, bearing the Meta logo. The scene is set on a dune.](https://i0.wp.com/craphound.com/images/big-tech-crabs.jpg?w=840&ssl=1)

## Technocarcinization ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#recapitulates-phylogeny))

"Carcinization" is a curious biological phenomenon: given enough time, across many environments, many species will evolve into crabs. The body-type of a crab, with its low center of gravity, sideways gait (useful for evading predators), ease of concealment and protected organs is suitable to many different environments:

[https://en.wikipedia.org/wiki/Carcinisation](https://en.wikipedia.org/wiki/Carcinisation)

Lately, I've watched the American Big Tech platforms as they underwent their own form of technocarcinization, which is when every tech company turns into Facebook.

![Image 3: A 2x2 grid. The vertical axis is labeled 'more surveillant.' The horizontal axis is labeled 'more control-freaky.' The top right quadrant has the Google logo. The top left, the Facebook and Instagram logos. The bottom left has the Apple logo. The bottom right has a Free Software Foundation Gnu.](https://i0.wp.com/craphound.com/images/big-tech-2x2a.jpg?w=840&ssl=1)

For a long time, it seemed to me that you could make sense of the tech platforms by placing them into one of four quadrants on a 2×2 grid, in which one axis denoted "control freakishness" and the other, "surveillance."

Each quadrant had its own canonical company. The most surveillant/least controlling company (top left) was Google. They would let you roam the whole wide internet and exert no control over your conduct, but would spy on you wherever you went. The least surveillant/most controlling company was Apple, who imprisoned you in its manicured walled garden, but promised never to spy on you. The non-spying/non-controlling option is free/open source tech (of course), which doesn't care what you do, and doesn't watch you do it. And the most spying, most controlling company was Facebook, a company whose products did everything they could to imprison you within their virtual walls, from which vantage they could effect maximal surveillance.

I've used this comparison many times over the years. I included in my 2023 book _The Internet Con_, along with the joke that Tiktok's position on the grid was so far up and to the right (maximum surveillance and control) that we'd had to put its logo on the back cover. Enough people took this joke seriously and wrote in to complain that they'd gotten a misprint without the logo that we added it to the paperback:

[https://www.versobooks.com/products/3035-the-internet-con](https://www.versobooks.com/products/3035-the-internet-con)

The grid was useful, until technocarcinization started to push _all_ the tech companies into that top right quadrant. Apple is no longer the company that protects you from surveillance – they're the company that spies on you, having secretly added a total surveillance system to the iPhone to target ads to you:

[https://pluralistic.net/2022/11/14/luxury-surveillance/#liar-liar](https://pluralistic.net/2022/11/14/luxury-surveillance/#liar-liar)

Apple can't even claim to protect you from third-party surveillance. Sure, they block Facebook from spying on you, but they have barred ICE Block, an app that tells you if there are ICE chuds hunting in your neighborhood, looking to kidnap you and send you to a concentration camp. Apple declared ICE mercenaries to be a "protected class":

[https://pluralistic.net/2025/10/06/rogue-capitalism/#orphaned-syrian-refugees-need-not-apply](https://pluralistic.net/2025/10/06/rogue-capitalism/#orphaned-syrian-refugees-need-not-apply)

And thanks to Apple's control-freakery – which prevents you from overriding Apple's decisions about your own devices – once Apple decides to spy on you or sell you out to fascist goons, there's nothing you can do about it:

[https://locusmag.com/feature/cory-doctorow-neofeudalism-and-the-digital-manor/](https://locusmag.com/feature/cory-doctorow-neofeudalism-and-the-digital-manor/)

Then there's Google, the company that ran a free-range livestock operation in which you could roam wherever you liked, because they could always find you when it was time for the slaughter. For years now, Google has been moving inexorably to the kind of control-freak nonsense that you used to only find in one of Apple's crystal prisons.

For example, every year or two, Google floats a proposal to use secure hardware in your device to rat you out if you've got an ad-blocker, privacy blocker, or other aftermarket add-on that lets you choose how you experience the digital world:

[https://pluralistic.net/2023/08/02/self-incrimination/#wei-bai-bai](https://pluralistic.net/2023/08/02/self-incrimination/#wei-bai-bai)

It's an idea they just can't quit, despite the fact that it's fucking abominable and everyone hates it:

[https://pluralistic.net/2026/06/12/compelled-speech/#quishing](https://pluralistic.net/2026/06/12/compelled-speech/#quishing)

Google used to pride itself in its ability to send you to the open web, viewing search as a conduit to other peoples' resources. Now, with AI search summaries, Google is harvesting the open web and then eating the seed corn, keeping searchers inside of Google's walled garden:

[https://pluralistic.net/2026/06/29/arsonist-firefighters/#im-feeling-lucky](https://pluralistic.net/2026/06/29/arsonist-firefighters/#im-feeling-lucky)

Google also took the idea of a free/open browser and ran with it, rehabilitating some discarded Apple code and turning it into Chrome, the internet's most dominant browser – by far. Now, Google is nerfing that browser's plug-in architecture in a way that blocks all kinds of user-tunable options, including and especially ad-blocking:

[https://protonprivacy.substack.com/p/google-is-finally-killing-ublock](https://protonprivacy.substack.com/p/google-is-finally-killing-ublock)

And Google has also announced that they're going to turn Android into an iPhone, making it both technically challenging and radioactively illegal for you to install software of your choosing on your own property:

[https://arstechnica.com/gadgets/2025/08/google-will-block-sideloading-of-unverified-android-apps-starting-next-year/](https://arstechnica.com/gadgets/2025/08/google-will-block-sideloading-of-unverified-android-apps-starting-next-year/)

Google is adopting every one of Apple's worst practices, and Apple is adopting all of Google's worst practices, and so they're both turning into Facebook: technocarcinization!

What's driving this technocarcinization? Well, the obvious answer is that the more Facebooklike a company becomes, the more ways there are for it to rip you off. Surveillance can be monetized by selling your data, by ad targeting, and by surveillance-based pricing and wage-suppression:

[https://pluralistic.net/2026/01/21/cod-marxism/#wannamaker-slain](https://pluralistic.net/2026/01/21/cod-marxism/#wannamaker-slain)

Control lets platforms block competing products, extract massive junk fees to the businesses they connect you to, and control repair and end-of-life, forcing you to replace hardware by blocking parts and independent service:

[https://pluralistic.net/2026/01/10/markets-are-regulations/#carney-found-a-spine](https://pluralistic.net/2026/01/10/markets-are-regulations/#carney-found-a-spine)

It turns out that "if you're not paying for the product, you're the product" is only half-right. The other half is, "even if you pay for the product, you're the product." Pay, don't pay: companies will productize anyone they can. And thanks to our enshittogenic policy environment – where the worst ideas of the worst people make the most money – you can _always_ be productized:

[https://pluralistic.net/2025/09/10/say-their-names/#object-permanence](https://pluralistic.net/2025/09/10/say-their-names/#object-permanence)

This is independent of the kind of person running the company. Facebook is run by Mark Zuckerberg, a cringe halfwit whose only successful idea was to offer Harvard bros a way of nonconsensually rating the fuckability of female undergrads. Everything he's done since was an acquisition (Whatsapp, Insta) or a flop (metaverse, Libra), or both (Oculus). Zuck owns the majority of the voting stock in the company, which means he has total control over its actions. He can ignore or fire his board members at will. He is the move fast/break things guy, whose every foolish whim can become policy that impacts billions of people.

By contrast, Google and Apple are no longer run by their flamboyant founders, who were every bit as prone to folly as Zuck. They were constrained by their shareholders, which meant that the blast-radius of Steve Jobs's worst ideas (like treating his otherwise curable cancer with green juice) were confined to his own person.

Today, Apple and Google are run by bloodless business sociopaths who go to enormous lengths to project an air of sober adulthood. And yet, these people – who would never be caught dead bow-hunting their own livestock or climbing into an MMA cage – have steered their companies into Facebook's quadrant on our enshittification 2×2.

I think this shows just how much the enshittification of tech is a matter of the policy environment, not the personalities of the people involved. Sure, the worst people imaginable run these companies, but the _reason_ they're able to yield to their most venal impulses and succeed is because the world has been re-arranged to make sociopathy and greed into fitness factors. We get technocarcinization because the most fit organism for a landscape without consequences is a zuckerbergian techno-crab:

[https://pluralistic.net/2023/07/28/microincentives-and-enshittification/](https://pluralistic.net/2023/07/28/microincentives-and-enshittification/)

What can we do about it? Well, we're going to have to remake the landscape to punish (rather than reward) enshittification:

[https://pluralistic.net/2026/01/01/39c3/#the-new-coalition](https://pluralistic.net/2026/01/01/39c3/#the-new-coalition)

And in the meantime, there is one inhabitant of the 2×2 that hasn't drifted up and to the right: free and open source software. It's still snugly nestled in the low-surveillance/low-control box, and if you live in that box, your life will be much, much better for it.

There's no better time to make the switch: with RAM and storage prices through the ceiling and OSes growing ever-more bloated with AI and spyware (but I repeat myself), this is _the_ moment to rehabilitate that old computer with Linux:

[https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm](https://www.fosslinux.com/158206/linux-on-older-hardware-revival-guide.htm)

The alternative is to be tormented by crabs no matter what you're trying to do or where you're trying to get to.

* * *

## Hey look at this ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#linkdump))

![Image 4](https://i0.wp.com/craphound.com/images/heylookatthis3.jpg?w=840&ssl=1)

*   How the AI bubble could pop and take down the global economy, according to the BIS [https://www.theregister.com/ai-and-ml/2026/06/29/how-the-ai-bubble-could-pop-and-take-down-the-global-economy-according-to-the-bis/5263793](https://www.theregister.com/ai-and-ml/2026/06/29/how-the-ai-bubble-could-pop-and-take-down-the-global-economy-according-to-the-bis/5263793)
*   To Decarbonize Quickly, Think Beyond Electrification [https://jacobin.com/2026/06/climate-electrification-homes-cars-decarbonization-tech](https://jacobin.com/2026/06/climate-electrification-homes-cars-decarbonization-tech)

*   Ireland is big tech’s lapdog – and that compromises its EU presidency [https://www.theguardian.com/commentisfree/2026/jun/30/ireland-big-tech-lapdog-eu-presidency-digital-sovereignty](https://www.theguardian.com/commentisfree/2026/jun/30/ireland-big-tech-lapdog-eu-presidency-digital-sovereignty)

*   Beyond Denial How Oil Execs Shaped a Landmark Climate Study [https://www.propublica.org/article/wedges-climate-research-bp-fossil-fuel-princeton](https://www.propublica.org/article/wedges-climate-research-bp-fossil-fuel-princeton)

*   US Supreme Court just blew up EU-US Data Transfers [https://noyb.eu/en/us-supreme-court-just-blew-eu-us-data-transfers](https://noyb.eu/en/us-supreme-court-just-blew-eu-us-data-transfers)

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 5: A shelf of leatherbound history books with a gilt-stamped series title, 'The World's Famous Events.'](https://i0.wp.com/craphound.com/images/worlds-famous-events.png?w=840&ssl=1)

## Object permanence ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#retro))

#15yrsago Print-on-demand and donations - report on DIY publishing business models [https://www.publishersweekly.com/pw/by-topic/columns-and-blogs/cory-doctorow/article/47858-with-a-little-help-heuristics.html](https://www.publishersweekly.com/pw/by-topic/columns-and-blogs/cory-doctorow/article/47858-with-a-little-help-heuristics.html)

#15yrsago Brazil rises up for free speech in 40 national demonstrations [https://globalvoices.org/2011/06/30/brazil-freedom-march/](https://globalvoices.org/2011/06/30/brazil-freedom-march/)

#10yrsago Grandad builds miniature backyard Disneyland [https://abcnews.com/Lifestyle/grandpa-builds-disneyland-inspired-backyard-theme-park-grandkids/story?id=40276633](https://abcnews.com/Lifestyle/grandpa-builds-disneyland-inspired-backyard-theme-park-grandkids/story?id=40276633)

#10yrsago Elizabeth Warren on monopolies in America, including Apple, Google, and Amazon [https://washingtonmonthly.com/2016/06/30/elizabeth-warrens-consolidation-speech-could-change-the-election/](https://washingtonmonthly.com/2016/06/30/elizabeth-warrens-consolidation-speech-could-change-the-election/)

#10yrsago White House plan to use data to shrink prison populations could be a racist dumpster fire [https://www.wired.com/2016/06/white-house-mission-shrink-us-prisons-data/](https://www.wired.com/2016/06/white-house-mission-shrink-us-prisons-data/)

#10yrsago Even if Moore's Law is "running out," there's still plenty of room at the bottom [https://www.technologyreview.com/2016/05/13/245938/moores-law-is-dead-now-what/](https://www.technologyreview.com/2016/05/13/245938/moores-law-is-dead-now-what/)

#10yrsago Black-hat hacker handles are often advertisements [https://www.wired.com/beyond-the-beyond/2016/07/web-semantics-modern-german-black-hat-hacker-handles/](https://www.wired.com/beyond-the-beyond/2016/07/web-semantics-modern-german-black-hat-hacker-handles/)

#10yrsago Spotify threatens to report Apple to competition regulators over App Store rejection [https://web.archive.org/web/20160630220301/https://www.recode.net/2016/6/30/12067578/spotify-apple-app-store-rejection](https://web.archive.org/web/20160630220301/https://www.recode.net/2016/6/30/12067578/spotify-apple-app-store-rejection)

#10yrsago Researchers find over 100 spying Tor nodes that attempt to compromise darknet sites [https://www.defcon.org/html/defcon-24/dc-24-speakers.html#Noubir](https://www.defcon.org/html/defcon-24/dc-24-speakers.html#Noubir)

#5yrsago Exxon lobbyist confesses to his crimes [https://pluralistic.net/2021/07/01/basilisk-tamers/#exxonknew](https://pluralistic.net/2021/07/01/basilisk-tamers/#exxonknew)

#5yrsago When the Sparrow Falls [https://pluralistic.net/2021/07/01/basilisk-tamers/#rage-against-the-machine](https://pluralistic.net/2021/07/01/basilisk-tamers/#rage-against-the-machine)

* * *

## Upcoming appearances ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#upcoming))

![Image 6: A photo of me onstage, giving a speech, pounding the podium.](https://i0.wp.com/craphound.com/images/appearances3.jpg?w=840&ssl=1)

*   London: Idler Festival, Jul 11

[https://www.idler.co.uk/festival/](https://www.idler.co.uk/festival/)
*   Edinburgh International Book Festival with Jimmy Wales, Aug 17

[https://www.edbookfest.co.uk/events/the-front-list-cory-doctorow-and-jimmy-wales](https://www.edbookfest.co.uk/events/the-front-list-cory-doctorow-and-jimmy-wales)

*   Sydney: The Festival of Dangerous Ideas, Aug 23-24

[https://festivalofdangerousideas.com/cory-doctorow/](https://festivalofdangerousideas.com/cory-doctorow/)

*   Melbourne: Enshittification at the Wheeler Centre, Aug 25

[https://www.wheelercentre.com/events-tickets/season-2026/cory-doctorow-enshittification](https://www.wheelercentre.com/events-tickets/season-2026/cory-doctorow-enshittification)

*   Brighton: The Reverse Centaur's Guide to Life After AI with Carole Cadwalladr (Brighton Dome), Sep 8

[https://brightondome.org/whats-on/LSC-cory-doctorow-the-reverse-centaurs-guide-to-life-after-ai/](https://brightondome.org/whats-on/LSC-cory-doctorow-the-reverse-centaurs-guide-to-life-after-ai/)

*   London: The Reverse Centaur's Guide to Life After AI with Riley Quinn (Foyle's Picadilly), Sep 9

[https://www.foyles.co.uk/events/enshittification-cory-doctorow-riley-quinn](https://www.foyles.co.uk/events/enshittification-cory-doctorow-riley-quinn)

*   South Bend: An Evening With Cory Doctorow (Notre Dame), Oct 6

[https://franco.nd.edu/events/2026/10/06/an-evening-with-cory-doctorow/](https://franco.nd.edu/events/2026/10/06/an-evening-with-cory-doctorow/)

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 7: A screenshot of me at my desk, doing a livecast.](https://i0.wp.com/craphound.com/images/recentappearances3.jpg?w=840&ssl=1)

## Recent appearances ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#recent))

*   Lawfare Daily

[https://www.youtube.com/watch?v=T1KIwaYRs1g](https://www.youtube.com/watch?v=T1KIwaYRs1g)
*   How to Think About AI (Organized Money)

[https://www.organizedmoney.fm/p/how-to-think-about-ai-with-cory-doctorow](https://www.organizedmoney.fm/p/how-to-think-about-ai-with-cory-doctorow)

*   Breaking Points

[https://www.youtube.com/watch?v=VJmUbkRqXeE](https://www.youtube.com/watch?v=VJmUbkRqXeE)

*   A.I. Enshittifies Everything (Slate)

[https://slate.com/podcasts/what-next-tbd/2026/06/cory-doctorow-thinks-a-i-is-overvalued-and-overrated-and-still-a-threat](https://slate.com/podcasts/what-next-tbd/2026/06/cory-doctorow-thinks-a-i-is-overvalued-and-overrated-and-still-a-threat)

*   A World That Just Might Work

[https://aworldthatjustmightwork.com/2026/06/cory-doctorow-ai-use-it-dont-buy-the-hype-dont-feed-the-bubble/](https://aworldthatjustmightwork.com/2026/06/cory-doctorow-ai-use-it-dont-buy-the-hype-dont-feed-the-bubble/)

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 8: A grid of my books with Will Stahle covers..](https://i0.wp.com/craphound.com/images/recent.jpg?w=840&ssl=1)

## Latest books ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#latest))

*   "The Reverse-Centaur's Guide to AI," a short book about being a better AI critic, Farrar, Straus and Giroux, June 2026

[https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/](https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/)
*   "Canny Valley": A limited edition collection of the collages I create for Pluralistic, self-published, September 2025 [https://pluralistic.net/2025/09/04/illustrious/#chairman-bruce](https://pluralistic.net/2025/09/04/illustrious/#chairman-bruce)

*   "Enshittification: Why Everything Suddenly Got Worse and What to Do About It," Farrar, Straus, Giroux, October 7 2025

[https://us.macmillan.com/books/9780374619329/enshittification/](https://us.macmillan.com/books/9780374619329/enshittification/)

*   "Picks and Shovels": a sequel to "Red Team Blues," about the heroic era of the PC, Tor Books (US), Head of Zeus (UK), February 2025 ([https://us.macmillan.com/books/9781250865908/picksandshovels](https://us.macmillan.com/books/9781250865908/picksandshovels)).

*   "The Bezzle": a sequel to "Red Team Blues," about prison-tech and other grifts, Tor Books (US), Head of Zeus (UK), February 2024 ([thebezzle.org](http://thebezzle.org/)).

*   "The Lost Cause:" a solarpunk novel of hope in the climate emergency, Tor Books (US), Head of Zeus (UK), November 2023 ([http://lost-cause.org](http://lost-cause.org/)).

*   "The Internet Con": A nonfiction book about interoperability and Big Tech (Verso) September 2023 ([http://seizethemeansofcomputation.org](http://seizethemeansofcomputation.org/)). Signed copies at Book Soup ([https://www.booksoup.com/book/9781804291245](https://www.booksoup.com/book/9781804291245)).

*   "Red Team Blues": "A grabby, compulsive thriller that will leave you knowing more about how the world works than you did before." Tor Books [http://redteamblues.com](http://redteamblues.com/).

*   "Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid, with Rebecca Giblin", on how to unrig the markets for creative labor, Beacon Press/Scribe 2022 [https://chokepointcapitalism.com](https://chokepointcapitalism.com/)

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 9: A cardboard book box with the Macmillan logo.](https://i0.wp.com/craphound.com/images/upcoming-books.jpg?w=840&ssl=1)

## Upcoming books ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#upcoming-books))

*   "The Post-American Internet," a geopolitical sequel of sorts to _Enshittification_, Farrar, Straus and Giroux, 2027 
*   "Unauthorized Bread": a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, April 20, 2027

*   "Enshittification, Why Everything Suddenly Got Worse and What to Do About It" (the graphic novel), Firstsecond, 2027

*   "The Memex Method," Farrar, Straus, Giroux, 2027

* * *

[](https://pluralistic.net/2026/07/01/ontogeny/)

![Image 10](https://i0.wp.com/craphound.com/images/colophon2.jpg?w=840&ssl=1)

## Colophon ([permalink](https://pluralistic.net/2026/07/01/ontogeny/#bragsheet))

Today's top sources:

**Currently writing: "The Post-American Internet," a sequel to "Enshittification," about the better world the rest of us get to have now that Trump has torched America. Fourth draft completed. Submitted to editor.**

*   A Little Brother short story about DIY insulin PLANNING

* * *

![Image 11](https://i0.wp.com/craphound.com/images/by.svg.png?w=840&ssl=1)

This work – excluding any serialized fiction – is licensed under a Creative Commons Attribution 4.0 license. That means you can use it any way you like, including commercially, provided that you attribute it to me, Cory Doctorow, and include a link to pluralistic.net.

[https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

Quotations and images are not included in this license; they are included either under a limitation or exception to copyright, or on the basis of a separate license. Please exercise caution.

* * *

## How to get Pluralistic:

Blog (no ads, tracking, or data-collection):

[Pluralistic.net](http://pluralistic.net/)

Newsletter (no ads, tracking, or data-collection):

[https://pluralistic.net/plura-list](https://pluralistic.net/plura-list)

Mastodon (no ads, tracking, or data-collection):

[https://mamot.fr/@pluralistic](https://mamot.fr/@pluralistic)

Bluesky (no ads, possible tracking and data-collection):

[https://bsky.app/profile/doctorow.pluralistic.net](https://bsky.app/profile/doctorow.pluralistic.net)

Medium (no ads, paywalled):

[https://doctorow.medium.com/](https://doctorow.medium.com/)

Tumblr (mass-scale, unrestricted, third-party surveillance and advertising):

[https://mostlysignssomeportents.tumblr.com/tagged/pluralistic](https://mostlysignssomeportents.tumblr.com/tagged/pluralistic)

"_When life gives you SARS, you make sarsaparilla_" -Joey "Accordion Guy" DeVilla

READ CAREFULLY: By reading this, you agree, on behalf of your employer, to release me from all obligations and waivers arising from any and all NON-NEGOTIATED agreements, licenses, terms-of-service, shrinkwrap, clickwrap, browsewrap, confidentiality, non-disclosure, non-compete and acceptable use policies ("BOGUS AGREEMENTS") that I have entered into with your employer, its partners, licensors, agents and assigns, in perpetuity, without prejudice to my ongoing rights and privileges. You further represent that you have the authority to release me from any BOGUS AGREEMENTS on behalf of your employer.

ISSN: 3066-764X

=== https://nesbitt.io/2026/07/01/the-cra-is-not-about-open-source.html ===
Title: The CRA is not about open source

URL Source: https://nesbitt.io/2026/07/01/the-cra-is-not-about-open-source.html

Published Time: 2026-07-01T10:00:00+00:00

Markdown Content:
At [FOSDEM](https://fosdem.org/2026/) in February and again at [UN Open Source Week](https://www.unopensource.org/) last week, the [Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) was the answer on offer whenever anyone asked what governments are doing about open source security, and the foundations and corporate advocates presenting it framed it as good news for open source. It is the largest piece of software legislation the EU has passed, the open source community spent two years lobbying over its text, and its main obligations come into force in December 2027.

It is also not about open source. Where open source appears in the text, it appears as an exemption, a component risk, a compliance contact, or a paperwork trail.

The CRA is a product-safety law in the [CE-mark](https://single-market-economy.ec.europa.eu/single-market/ce-marking_en) family, the same regime that already covers toys, radio equipment and machinery: rules a manufacturer must meet before selling a product in the EU, with a conformity mark at the end. The CRA extends that to anything with software in it. In [the previous post](https://nesbitt.io/2026/06/30/taking-roads-and-bridges-literally.html) I described this class of regulation as requiring haulage firms to certify which bridges their lorries crossed while employing no bridge inspectors, and the CRA is the regulation most often held up as the counterexample.

## Scope

The things the CRA defines are products, the companies that make or sell them, and components. There is nothing in it corresponding to a project, a package, a registry, or a maintainer. Open source is visible in the regulation only as a property a component of a regulated product can have, so in the CRA’s terms there is no OpenSSL, only products that incorporate OpenSSL.

Non-commercial open source is carved out of scope, which took a lot of lobbying and has been treated since as a win for the community. But exclusion from a product regulation is not the same as benefiting from it. A project outside the CRA’s scope is in the same position as one the drafters had never heard of.

The regulation establishes no fund and no inspection or maintenance body, and nothing in it requires a manufacturer to contribute upstream. The exemption is the edge of what product law can reach: software nobody is selling offers nothing for a market regulation to attach to.

The phrase “supply chain” appears in the text in its product-law sense, meaning the chain of companies who put a good on the market and can each be held responsible for it. That is a different thing from the transitive dependency graph the same phrase means in open source, and reading the regulation as if it governs the second because the vocabulary overlaps is a category error.

## Dependencies

The clause that bears most directly on open source dependencies requires a manufacturer to exercise due diligence when pulling in third-party components, open source included. A manufacturer discharging that duty has a menu of options:

*   vendor the dependency and patch it in-house
*   replace it with a different dependency
*   buy a commercially supported distribution that comes with its own paperwork
*   run a scanner against the dependency tree and file the output

None of those routes money to the upstream author, because the rational response to liability for a component is to reduce exposure to it rather than to invest in it. A haulage firm told it is answerable for the state of every bridge on its route will plan routes with fewer bridges on them before it considers starting a bridge-repair division. When open source licence terms became a perceived corporate risk, the tooling that appeared was [licence scanners](https://en.wikipedia.org/wiki/Software_composition_analysis) and component-replacement policies, and security liability is the same shape of problem.

The closest the text gets to upstream is a clause requiring a manufacturer who finds a vulnerability in a component to report it to the maintainer. That duty assumes a maintainer is still there to receive it, which is what a maintenance regime would ensure and a product regulation cannot.

## Stewards

The steward category covers organisations that support open source intended for commercial use without themselves selling a product. A steward’s obligations are lighter than a manufacturer’s: have a security policy, cooperate with regulators on request, and handle vulnerability reports for the projects it looks after.

Those are the duties of an organisation that would otherwise be a gap in a manufacturer’s paperwork, which in bridge terms means requiring an existing maintenance crew to post a contact number so that a haulier filling in forms has someone to name. Nothing in the steward provisions hires that crew or appoints an inspector, and the lighter obligations are still organised around the manufacturer’s product.

For the steward category to route money to open source, manufacturers would need to prefer steward-backed components enough to pay for them. The regulation gives a manufacturer no reason to: its due diligence can be discharged by any of the routes in the previous section with no steward involved. Anyone who does want to buy component assurance can already get it from commercial redistributors. [Red Hat](https://www.redhat.com/) has been selling supported open source for over two decades, and [Chainguard](https://www.chainguard.dev/) sells hardened images with the SBOM and vulnerability handling needed for a CRA technical file. The nearest thing to a saleable steward output is Article 25’s voluntary security attestation, left to a future delegated act. Becoming a steward today adds obligations to a foundation without creating anything a manufacturer is obliged to buy from it.

## SBOMs

The SBOM requirement asks for top-level dependencies “at the very least,” which makes the transitive graph optional, and the SBOM goes into the manufacturer’s technical file alongside the rest of the compliance paperwork. That file is held by the manufacturer and handed to a regulator on request, with no right of access for consumers, researchers, or maintainers. This is how [CE-mark technical files](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022XC0629(04)) have always worked: a private record between the manufacturer and whoever might one day audit it.

The SBOM that results is a liability artifact rather than a transparency instrument:

*   the maintainer of a library inside a CE-marked product does not learn from the CRA process that they are there
*   a researcher cannot use CRA filings to map which commercial products depend on which open source projects
*   a consumer comparing two products cannot see which has the better-maintained dependency tree

The CRA will not, to take a concrete case, put a public SBOM for Windows anywhere a member of the public can read it. The [National Bridge Inventory](https://infobridge.fhwa.dot.gov/) from the previous post is open to anyone, and because the bridge regime attaches to the function a structure performs, the privately held Ambassador Bridge is federally inspected regardless of title. A library inside thousands of CE-marked products gets no equivalent record, because the CRA’s trigger is commercial activity and its technical file is a sealed dossier for apportioning fault after an incident.

## Implementation

The machinery the CRA sets running is all on the product side: the Commission will sort products into risk classes, [ENISA](https://www.enisa.europa.eu/) will run a reporting platform for manufacturers to notify exploited vulnerabilities in their own products, member states will appoint enforcement bodies, and [CEN, CENELEC and ETSI](https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation) are writing the standards manufacturers will be assessed against. None of that touches anything upstream of the manufacturer, because the regulation defines nothing there.

The second-order effects that do reach open source are modest: SBOM tooling will mature because more manufacturers need to produce SBOMs, though [Executive Order 14028](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity) had already pushed that along. Exploited-vulnerability reporting will be quicker in the specific case of a manufacturer notifying ENISA about its own product. Neither of those is particular to open source or acts on the upstream project where a vulnerability originates.

When [Log4Shell](https://en.wikipedia.org/wiki/Log4Shell) prompted a European policy response, the instrument that came back was product law, which is structurally incapable of acting on the infrastructure that prompted it. The CRA does open source little direct harm, and the exemptions the community fought for are about as good as exemptions get.

The cost is that “we passed the CRA” is now available as the answer when open source maintenance comes up: a regulation with no maintenance regime in it occupies the slot where one would go. The open source community made the CRA an open source story through its own lobbying, and two years on is still reading itself into a text whose subject is manufacturers and consumers.
Title: It rather involved being on the other side of this airtight hatchway: Changing administrative settings

URL Source: https://devblogs.microsoft.com/oldnewthing/20260701-00/?p=112498

Published Time: 2026-07-01T14:00:00+00:00

Markdown Content:
A security vulnerability report arrived that went roughly like this:

> An attacker can bypass security policies by modifying the following registry keys to disable ⟦security feature 1⟧ and ⟦security feature 2⟧.

The statement is true, but what they don’t mention is that administrator privileges are required to modify those keys. This is like saying that a door lock is insecure because you can open the door from the inside. If you are inside, then you have already gotten past the door!

Indeed, the purpose of those keys is to define the security policy in the first place! So it boils down to “It’s a security vulnerability that an administrator can change a security policy.”

What the security researcher found was that if your system has been compromised, the first guy who gets into your inner sanctum can make your system even more vulnerable.¹ If you assume that the attacker has full control, then it’s not surprising that they control everything.

¹ Isn’t this the plot to half of the sci-fi movies ever made? The plucky hero sneaks behind enemy lines in order to disable the bad guys’ shields long enough to let the rest of the team in. This isn’t a security flaw in the shields. It’s a security flaw in whatever was supposed to protect the switch that turns off the shields.

The sci-fi movie analogy would be “If we can get to the switch that turns off the shields, then we can turn them off!”

Well, yeah. The hard part is getting into the room that has the switch.

It rather involved being on the other side of this airtight hatchway.

**Bonus chatter**: This is a repeat of [It rather involved being on the other side of the airtight hatchway: Disabling a security feature as an administrator](https://devblogs.microsoft.com/oldnewthing/20240806-00/?p=110103 "It rather involved being on the other side of the airtight hatchway: Disabling a security feature as an administrator"), but this type of bogus vulnerability report happens so much, I wrote it up again before I realized that it was a duplicate.

## Author

![Image 1: Raymond Chen](https://devblogs.microsoft.com/oldnewthing/wp-content/uploads/sites/38/2019/02/RaymondChen_5in-150x150.jpg)

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.
Title: The earliest surviving Tom’s Hardware Guide article

URL Source: https://dfarq.homeip.net/the-earliest-surviving-toms-hardware-guide-article/

Published Time: 2026-07-01T11:00:26+00:00

Markdown Content:
The earliest dated article still active on Tom’s Hardware Guide is dated July 1, 1996. It was an article about CPU softmenus, something we pretty much take for granted today, but at the time was only available on select Abit and QDI motherboards. I’m not 100% certain that Tom’s Hardware Guide made its debut on July 1, 1996. In fact, I’m pretty sure it didn’t. But without a firm birth date, today’s as good of a day as any to look back at the very early days of a venerable PC hardware website.

[![Image 1: Tom's Hardware Guide as it appeared in Dec 1996](https://i0.wp.com/dfarq.homeip.net/wp-content/uploads/2025/04/toms-hardware-guide-in-dec-1996.jpg?resize=300%2C225&ssl=1)](https://dfarq.homeip.net/the-earliest-surviving-toms-hardware-guide-article/toms-hardware-guide-in-dec-1996/)

Here’s Tom’s Hardware Guide in all its late 1996 glory.

The article referred more to [Abit](https://dfarq.homeip.net/what-happened-to-abit-motherboards/) than to QDI. [Dr. Thomas Pabst](https://dfarq.homeip.net/whatever-happened-to-dr-thomas-pabst/) even said the QDI softmenu was just something he’d heard about, that he was using an Abit motherboard. Maybe he had more than one Abit motherboard, but in these early days, the hardware makers weren’t sending him stuff. He was reviewing stuff he bought with his own money.

## What a CPU softmenu is

If you’ve built your own PC using off-the-shelf parts, you’ve probably used a CPU softmenu. When you insert the CPU, the CPU doesn’t necessarily come up running at full speed. You have to go into the BIOS and tell it what speed to run the CPU at. Depending on the board, it may let you overclock, or it may not.

But this was a really new and novel thing in 1996. Before the CPU softmenu came about, you had to set your CPU using jumpers or DIP switches–usually jumpers–on the motherboard. Sometimes there would be a legend printed on the motherboard to help you out. But usually, you had to dig out a manual and find which jumpers set the bus speed, multiplier, and voltage. Somehow I never damaged a CPU by setting my jumpers wrong, but the opportunity was there.

Jumpers were cool, because in some cases, jumper combinations that weren’t in the manual did something. Another early Tom’s Hardware article told how to get an 83 MHz bus speed out of certain Intel 430HX-based Socket 7 motherboards.

The motherboard he was using didn’t have the 83 MHz bus speed, so it must not have been the legendary Abit IT5H. The date on his review of that board is January 1997, so a few months later. I actually bought that board on the basis of his review.

But being able to change CPU settings without opening the case and fumbling around for jumpers was very nice. It wasn’t something I needed to do often. But since I could do it without opening the case, I actually found myself doing it more. So did he, like, every time he booted into DOS.

## Was this the first Tom’s Hardware article?

I really don’t think the CPU softmenu article wsa the very first Tom’s Hardware article. First, going to archive.org and viewing the oldest snapshot of the page and looking at the news link, he has diary entries going back to June 26.

### The diary entries

In the truest ’90s Internet fashion, he talks as much about his personal life as about the site. It was a very different time, yes. Since he could talk about his girlfriend being in the hospital in June 1996, he had a following before that, and, therefore, articles before that. A really popular web site only had a few thousand regular readers at that point, so a popular website was like living in a small neighborhood or town where everyone knew what was going on with everyone else. Those days of innocence are long gone. You don’t dare divulge details like that lest foreign adversaries snarf them up and use them against you later.

### Evidence he already had visitors and traffic

But the third paragraph of the article gives an even stronger implication this wasn’t his first:

> However, for the performance hungry visitors of my website this is the perfect way to tweak the system performance from the comfort of your chair. You even can run Quake at higher settings as Windows95, which wouldn’t run at the same settings, without ever opening your computer case.

What he was saying in other words was that you could clock your system higher under DOS than under Windows 95, so when you booted into DOS to play Quake or another [DOS game](https://dfarq.homeip.net/what-is-a-dos-game/), you could overclock higher for your gaming session, then switch back when you were ready to load Windows again, without ever having to open your case.

In 1996, when you were publishing your first piece of content, you didn’t assume you had visitors. It took time for people to find you, and in those pre-[Google](https://dfarq.homeip.net/google-incorporated-september-4-1998/) days, people generally found you before the search engines did. If you didn’t have an audience before the search engines found you, chances are the search engines wouldn’t boost you all that much. Just making that statement alone suggests he already had traffic.

![Image 2](https://i0.wp.com/dfarq.homeip.net/wp-content/uploads/2017/06/dave_farquhar_181px.jpg?resize=100%2C100&ssl=1)

David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
