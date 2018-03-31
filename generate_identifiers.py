import os, subprocess, base64, hashlib

def GG_template(completeness, GH_list):
    template = "<Genotype:" + completeness + ":["
    for GH in GH_list:
        template = template + "<Identifier:" + GH + ">;"
    return template[:-1] + "]>"

def GH_template(completeness, GA_list):
    template = "<Haplotype:" + completeness + ":["
    for GA in GA_list:
        template = template + "<Identifier:" + GA + ">;"
    return template[:-1] + "]>"

def GA_template(GL, state):
    return "<Allele:<Identifier:" + GL + ">:" + state + ">"

def GL_template(GS, interval):
    return "<Location:<Identifier:" + GS + ">:<Interval:" + interval + ">>"

def digest(blob, n=24):
    d = hashlib.sha512(blob).digest()
    return base64.urlsafe_b64encode(d[:n]).decode("ASCII")

def vcf_to_vmc(seqs, chrs, intervals, states):
    results = []
    for i in range(len(chrs)):
        chr = int(chrs[i]) - 1
        #Generate the location identifier
        GL = "VMC:GL_" + digest(GL_template(seqs[chr],intervals[i]).encode("ASCII"))
        #Generate the allele identifier
        GA = "VMC:GA_" + digest(GA_template(GL,states[i]).encode("ASCII"))
        #Compile them into an appropriate string
        results.append(";VMCGSID=" + seqs[chr] + ";VMCGLID=" + GL + ";VMCGAID=" + GA)
    return results

def json_to_vmc(seqs, accs, chrs, intervals, states):
    results = []
    for i in range(len(chrs)):
        chr = int(chrs[i]) - 1
        #Generate the location identifier
        GL = "VMC:GL_" + digest(GL_template(seqs[chr],intervals[i]).encode("ASCII"))
        #Generate the allele identifier
        GA = "VMC:GA_" + digest(GA_template(GL,states[i]).encode("ASCII"))
        results.append(GL + '\t' + intervals[i] + '\t' + seqs[chr] + '\t' + GA + '\t' + states[i] + '\t' + accs[chr] + "\tNCBI")
    return results
