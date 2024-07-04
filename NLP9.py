## Python Nltk program to get overview of tagset
import nltk
nltk.download('tagsets')
print("\n Overview of the tagset:")
print(nltk.help.brown_tagset())
print("\n Details of specific tagset")
print(nltk.help.brown_tagset(r"NNS"))
print("\n Details on several related tagsets,using regular expressions:")
nltk.help.brown_tagset(r'WP*')

## output
#     'tain't

[ PPSS+HV: pronoun, personal, nominative, not 3rd person singular + verb 'to have', uninflected present tense
        I've we've they've you've
    PPSS+HVD: pronoun, personal, nominative, not 3rd person singular + verb 'to have', past tense
        I'd you'd we'd they'd
    PPSS+MD: pronoun, personal, nominative, not 3rd person singular + modal auxillary
        you'll we'll I'll we'd I'd they'll they'd you'd
    PPSS+VB: pronoun, personal, nominative, not 3rd person singular + verb 'to verb', uninflected present tense
        y'know
    QL: qualifier, pre
        well less very most so real as highly fundamentally even how much
        remarkably somewhat more completely too thus ill deeply little overly
        halfway almost impossibly far severly such ...
    QLP: qualifier, post
        indeed enough still 'nuff
    RB: adverb
        only often generally also nevertheless upon together back newly no
        likely meanwhile near then heavily there apparently yet outright fully
        aside consistently specifically formally ever just ...
    RB$: adverb, genitive
        else's
    RB+BEZ: adverb + verb 'to be', present tense, 3rd person singular
        here's there's
    RB+CS: adverb + conjunction, coordinating
        well's soon's
    RBR: adverb, comparative
        further earlier better later higher tougher more harder longer sooner
        less faster easier louder farther oftener nearer cheaper slower tighter
        lower worse heavier quicker ...
    RBR+CS: adverb, comparative + conjunction, coordinating
        more'n
    RBT: adverb, superlative
        most best highest uppermost nearest brightest hardest fastest deepest
        farthest loudest ...
    RN: adverb, nominal
        here afar then
    RP: adverb, particle
        up out off down over on in about through across after
    RP+IN: adverb, particle + preposition
        out'n outta
    TO: infinitival to
        to t'
    TO+VB: infinitival to + verb, infinitive
        t'jawn t'lah
    UH: interjection
        Hurrah bang whee hmpf ah goodbye oops oh-the-pain-of-it ha crunch say
        oh why see well hello lo alas tarantara rum-tum-tum gosh hell keerist
        Jesus Keeeerist boy c'mon 'mon goddamn bah hoo-pig damn ...
    VB: verb, base: uninflected present, imperative or infinitive
        investigate find act follow inure achieve reduce take remedy re-set
        distribute realize disable feel receive continue place protect
        eliminate elaborate work permit run enter force ...
    VB+AT: verb, base: uninflected present or infinitive + article
        wanna
    VB+IN: verb, base: uninflected present, imperative or infinitive + preposition
        lookit
    VB+JJ: verb, base: uninflected present, imperative or infinitive + adjective
        die-dead
    VB+PPO: verb, uninflected present tense + pronoun, personal, accusative
        let's lemme gimme
    VB+RP: verb, imperative + adverbial particle
        g'ahn c'mon
    VB+TO: verb, base: uninflected present, imperative or infinitive + infinitival to
        wanta wanna
    VB+VB: verb, base: uninflected present, imperative or infinitive; hypenated pair
        say-speak
    VBD: verb, past tense
        said produced took recommended commented urged found added praised
        charged listed became announced brought attended wanted voted defeated
        received got stood shot scheduled feared promised made ...
    VBG: verb, present participle or gerund
        modernizing improving purchasing Purchasing lacking enabling pricing
        keeping getting picking entering voting warning making strengthening
        setting neighboring attending participating moving ...
    VBG+TO: verb, present participle + infinitival to
        gonna
    VBN: verb, past participle
        conducted charged won received studied revised operated accepted
        combined experienced recommended effected granted seen protected
        adopted retarded notarized selected composed gotten printed ...
    VBN+TO: verb, past participle + infinitival to
        gotta
    VBZ: verb, present tense, 3rd person singular
        deserves believes receives takes goes expires says opposes starts
        permits expects thinks faces votes teaches holds calls fears spends
        collects backs eliminates sets flies gives seeks reads ...
    WDT: WH-determiner
        which what whatever whichever whichever-the-hell
    WDT+BER: WH-determiner + verb 'to be', present tense, 2nd person singular or all persons plural       
        what're
    WDT+BER+PP: WH-determiner + verb 'to be', present, 2nd person singular or all persons plural + pronoun, personal, nominative, not 3rd person singular
        whaddya
    WDT+BEZ: WH-determiner + verb 'to be', present tense, 3rd person singular
        what's
    WDT+DO+PPS: WH-determiner + verb 'to do', uninflected present tense + pronoun, personal, nominative, not 3rd person singular
        whaddya
    WDT+DOD: WH-determiner + verb 'to do', past tense
        what'd
    WDT+HVZ: WH-determiner + verb 'to have', present tense, 3rd person singular
        what's
    WP$: WH-pronoun, genitive
        whose whosever
    WPO: WH-pronoun, accusative
        whom that who
    WPS: WH-pronoun, nominative
        that who whoever whosoever what whatsoever
    WPS+BEZ: WH-pronoun, nominative + verb 'to be', present, 3rd person singular
        that's who's
    WPS+HVD: WH-pronoun, nominative + verb 'to have', past tense
        who'd
    WPS+HVZ: WH-pronoun, nominative + verb 'to have', present tense, 3rd person singular
        who's that's
    WPS+MD: WH-pronoun, nominative + modal auxillary
        who'll that'd who'd that'll
    WQL: WH-qualifier
        however how
    WRB: WH-adverb
        however when where why whereby wherever how whenever whereon wherein
        wherewith wheare wherefore whereof howsabout
    WRB+BER: WH-adverb + verb 'to be', present, 2nd person singular or all persons plural
        where're
    WRB+BEZ: WH-adverb + verb 'to be', present, 3rd person singular
        how's where's
    WRB+DO: WH-adverb + verb 'to do', present, not 3rd person singular
        howda
    WRB+DOD: WH-adverb + verb 'to do', past tense
        where'd how'd
    WRB+DOD*: WH-adverb + verb 'to do', past tense, negated
        whyn't
    WRB+DOZ: WH-adverb + verb 'to do', present tense, 3rd person singular
        how's
    WRB+IN: WH-adverb + preposition
        why'n
    WRB+MD: WH-adverb + modal auxillary
        where'd
    None

    Details of specific tagset
    NNS: noun, plural, common
        irregularities presentments thanks reports voters laws legislators
        years areas adjustments chambers $100 bonds courts sales details raises
        sessions members congressmen votes polls calls ...
    None

    Details on several related tagsets,using regular expressions:
    WDT: WH-determiner
        which what whatever whichever whichever-the-hell
    WDT+BER: WH-determiner + verb 'to be', present tense, 2nd person singular or all persons plural       
        what're
    WDT+BER+PP: WH-determiner + verb 'to be', present, 2nd person singular or all persons plural + pronoun, personal, nominative, not 3rd person singular
        whaddya
    WDT+BEZ: WH-determiner + verb 'to be', present tense, 3rd person singular
        what's
    WDT+DO+PPS: WH-determiner + verb 'to do', uninflected present tense + pronoun, personal, nominative, not 3rd person singular
        whaddya
    WDT+DOD: WH-determiner + verb 'to do', past tense
        what'd
    WDT+HVZ: WH-determiner + verb 'to have', present tense, 3rd person singular
        what's
    WP$: WH-pronoun, genitive
        whose whosever
    WPO: WH-pronoun, accusative
        whom that who
    WPS: WH-pronoun, nominative
        that who whoever whosoever what whatsoever
    WPS+BEZ: WH-pronoun, nominative + verb 'to be', present, 3rd person singular
        that's who's
    WPS+HVD: WH-pronoun, nominative + verb 'to have', past tense
        who'd
    WPS+HVZ: WH-pronoun, nominative + verb 'to have', present tense, 3rd person singular
        who's that's
    WPS+MD: WH-pronoun, nominative + modal auxillary
        who'll that'd who'd that'll
    WQL: WH-qualifier
        however how
    WRB: WH-adverb
        however when where why whereby wherever how whenever whereon wherein
        wherewith wheare wherefore whereof howsabout
    WRB+BER: WH-adverb + verb 'to be', present, 2nd person singular or all persons plural
        where're
    WRB+BEZ: WH-adverb + verb 'to be', present, 3rd person singular
        how's where's
    WRB+DO: WH-adverb + verb 'to do', present, not 3rd person singular
        howda
    WRB+DOD: WH-adverb + verb 'to do', past tense
        where'd how'd
    WRB+DOD*: WH-adverb + verb 'to do', past tense, negated
        whyn't
    WRB+DOZ: WH-adverb + verb 'to do', present tense, 3rd person singular
        how's
    WRB+IN: WH-adverb + preposition
        why'n
    WRB+MD: WH-adverb + modal auxillary
    where'd ]