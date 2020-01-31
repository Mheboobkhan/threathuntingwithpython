#prerequisite tshark

import os 
#Importing the pcap file 

in_file = input ("Enter the Path/Name of pcap file ::")
out_file = input ("Name the output file ::")

#Creating tuples for all wireshark filters

def pcap_template (To_show):
    
    Ethernet = ('eth.addr','eth.dst','eth.ig','eth.len','eth.lg','eth.src','eth.trailer','eth.type')
    ARP =('arp.dst.hw_mac','arp.dst.proto_ipv4','arp.hw.size','arp.hw.type','arp.opcode','arp.proto.size','arp.proto.type','arp.src.hw_mac','arp.src.proto_ipv4')
    IPv4 = ('ip.addr','ip.checksum','ip.checksum_bad','ip.checksum_good','ip.dsfield','ip.dsfield.ce','ip.dsfield.dscp','ip.dsfield.ect','ip.dst','ip.dst_host','ip.flags','ip.flags.df','ip.flags.mf','ip.flags.rb','ip.frag_offset','ip.fragment','ip.fragment.error','ip.fragment.multipletails','ip.fragment.overlap','ip.fragment.overlap.conflict','ip.fragment.toolongfragment','ip.fragments','ip.hdr_len','ip.host','ip.id','ip.len','ip.proto','ip.reassembled_in','ip.src','ip.src_host','ip.tos','ip.tos.cost','ip.tos.delay','ip.tos.precedence','ip.tos.reliability','ip.tos.throughput','ip.ttl','ip.version')
    TCP = ('tcp.ack','tcp.checksum','tcp.checksum_bad','tcp.checksum_good','tcp.continuation_to','tcp.dstport','tcp.flags','tcp.flags.ack','tcp.flags.cwr','tcp.flags.ecn','tcp.flags.fin','tcp.flags.push','tcp.flags.reset','tcp.flags.syn','tcp.flags.urg','tcp.hdr_len','tcp.len','tcp.nxtseq','tcp.options','tcp.options.cc','tcp.options.ccecho','tcp.options.ccnew','tcp.options.echo','tcp.options.echo_reply','tcp.options.md5','tcp.options.mss','tcp.options.mss_val','tcp.options.qs','tcp.options.sack','tcp.options.sack_le','tcp.options.sack_perm','tcp.options.sack_re','tcp.options.time_stamp','tcp.options.wscale','tcp.options.wscale_val','tcp.pdu.last_frame','tcp.pdu.size','tcp.pdu.time','tcp.port','tcp.reassembled_in','tcp.segment','tcp.segment.error','tcp.segment.multipletails','tcp.segment.overlap','tcp.segment.overlap.conflict','tcp.segment.toolongfragment','tcp.segments','tcp.seq','tcp.srcport','tcp.time_delta','tcp.time_relative','tcp.urgent_pointer','tcp.window_size')
    UDP = ('udp.checksum','udp.checksum_bad','udp.checksum_good','udp.dstport','udp.length','udp.port','udp.srcport')
    ICMP = ('icmp.checksum','icmp.checksum_bad','icmp.code','icmp.ident','icmp.mtu','icmp.redir_gw','icmp.seq','icmp.type')
    ICMPv6 = ('icmpv6.all_comp','icmpv6.checksum','icmpv6.checksum_bad','icmpv6.code','icmpv6.comp','icmpv6.haad.ha_addrs ','icmpv6.identifier','icmpv6.option','icmpv6.option.cga','icmpv6.option.length','icmpv6.option.name_type.fqdn','icmpv6.option.name_x501','icmpv6.option.rsa.key_hash','icmpv6.option.type','icmpv6.ra.cur_hop_limit','icmpv6.ra.reachable_time','icmpv6.ra.retrans_timer ','icmpv6.ra.router_lifetime','icmpv6.recursive_dns_serv','Icmpv6.type')
    HTTP = ('http.accept','http.accept_encoding','http.accept_language','http.authbasic','http.authorization','http.cache_control','http.connection','http.content_encoding','http.content_length','http.content_type','http.cookie','http.date','http.host','http.last_modified','http.location','http.notification','http.proxy_authenticate','http.proxy_authorization','http.proxy_connect_host','http.proxy_connect_port','http.referer','http.request','http.request.method','http.request.uri','http.request.version','http.response','http.response.code','http.server','http.set_cookie','http.transfer_encoding','http.user_agent','http.www_authenticate','http.x_forwarded_for')
    
    if (To_show == 'Ethernet'):
        print (Ethernet)
    elif (To_show == 'IPv4'):
        print (IPv4)
    elif (To_show == 'UDP'):
        print(UDP)
    elif (To_show == 'TCP'):
        print(TCP)
    elif (To_show == 'ICMP'):
        print(ICMP)
    elif (To_show == 'ICMPv6'):
        print(ICMPv6)
    elif (To_show == 'HTTP'):
        print (HTTP)
    else :
        print ('Select a valid entry !!!')

print ('='*23)
print ('choose the options')
#Taking the format to convert
exten = input  (' 1 >> .txt \n 2 >> .csv \n 3 >> wireshark filters list \n')
#

#Taking filter input form users
def get_filter ():
    CSV = list (map (str,input ('\nEnter the filter fields seprated by space \n').strip().split()))
    line = ' '
    for k in range (0,len(CSV)):
        line = line +'-e '+CSV[k] + ' '
    return line
    
def Converter (i):
    if (i == '1'):
        line_txt = get_filter()
        os.system ('tshark -r '+in_file +' -T fields '+line_txt+'-E header=y '+' > '+out_file+'.txt')
        print (out_file+'.txt is created')
        
    elif (i == '2'):
        line_csv=get_filter()
        os.system ('tshark -r '+in_file +' -T fields '+line_csv+'-E header=y -E separator=,'+' > '+out_file+'.csv')
        print (out_file+'.csv is created')
    
    elif (i == '3'):
        print('choose filters to see all fields')
        filter_choice = str(input('\nEthernet\nIPv4\nTCP\nUDP\nICMP\nICMPv6\nHTTP\n>>>'))
        pcap_template(filter_choice)
        
    else :    
        print ('invalid option')

Converter(exten)

