# Map of From address to boat ID in the system
USER_MAP = {
    'adamaflynn@gmail.com': 'reverence',
    '881632574063@msg.iridium.com': 'reverence',
}

PROPER_NAME = {
    'reverence': "S/V Reverence"
}

FAKE_EMAIL = """Delivered-To: adamaflynn@gmail.com
Received: by 10.103.81.221 with SMTP id m90csp909044vsg;
        Mon, 19 Sep 2016 02:55:52 -0700 (PDT)
X-Received: by 10.55.7.7 with SMTP id 7mr29564600qkh.228.1474278952053;
        Mon, 19 Sep 2016 02:55:52 -0700 (PDT)
Return-Path: <881632574063@msg.iridium.com>
Received: from vps.ispeakofcake.com (vps.ispeakofcake.com. [216.22.60.97])
        by mx.google.com with ESMTPS id 191si17171414qki.210.2016.09.19.02.55.51
        for <adamaflynn@gmail.com>
        (version=TLS1 cipher=AES128-SHA bits=128/128);
        Mon, 19 Sep 2016 02:55:51 -0700 (PDT)
Received-SPF: neutral (google.com: 216.22.60.97 is neither permitted nor denied by best guess record for domain of 881632574063@msg.iridium.com) client-ip=216.22.60.97;
Authentication-Results: mx.google.com;
       spf=neutral (google.com: 216.22.60.97 is neither permitted nor denied by best guess record for domain of 881632574063@msg.iridium.com) smtp.mailfrom=881632574063@msg.iridium.com
Received: from istmlb.iridium.com ([208.25.12.85]:34687 helo=istwg02.iridium.com) by vps.ispeakofcake.com with esmtp (Exim 4.87) (envelope-from <881632574063@msg.iridium.com>) id 1blvId-0002x4-0Y for Adam@flynngroup.net; Mon, 19 Sep 2016 05:55:51 -0400
Received: from smsc01.gw01.iwcs.net (unknown [10.1.23.21]) by istwg02.iridium.com (Extensible Content Security) with ESMTP id 035CE3CC7EF82A61 for <Adam@flynngroup.net>; Mon, 19 Sep 2016 09:54:46 +0000 (GMT)
Received: from msg.iridium.com (localhost [127.0.0.1]) by smsc01.gw01.iwcs.net (8.14.9+Sun/8.14.9) with SMTP id u8J9sqTT026553 for <Adam@flynngroup.net>; Mon, 19 Sep 2016 09:54:52 GMT
Message-Id: <201609190954.u8J9sqTT026553@smsc01.gw01.iwcs.net>
Date: Mon, 19 Sep 2016
  09:54:52 +0000
From: 881632574063@msg.iridium.com
To: Adam@flynngroup.net
Subject: SMS from 881632574063@msg.iridium.com
X-Mailer: Iridium SMSC
Reply-To: 881632574063@msg.iridium.com
X-Spam-Status: No, score=-3.8
X-Spam-Score: -37
X-Spam-Bar: ---
X-Ham-Report: Spam detection software, running on the system "vps.ispeakofcake.com", has NOT identified this incoming email as spam.
  The original message has been attached to this so you can view it or label similar future email.
  If you have any questions, see root\@localhost for details.
  Content preview:
  I am here Lat+37.128828 Lon+26.857672 Alt000ft GPS Sats seen
    04 http://map.iridium.com/m?lat=37.128828&lon=26.857672 Sent via Iridium
   GO! [...]
   Content analysis details:
   (-3.8 points, 5.0 required)
   pts rule name
              description ---- ---------------------- -------------------------------------------------- -2.3 RCVD_IN_DNSWL_MED
      RBL: Sender listed at http://www.dnswl.org/, medium
                              trust
                             [208.25.12.85 listed in list.dnswl.org]
  0.0 FROM_LOCAL_HEX
         From: localpart has long hexadecimal sequence
  0.0 FROM_LOCAL_DIGITS
      From: localpart has long digit sequence
  0.0 T_SPF_HELO_TEMPERROR
   SPF: test of HELO record failed (temperror) -3.1 RP_MATCHES_RCVD
        Envelope sender domain matches handover relay domain -1.9 BAYES_00
               BODY: Bayes spam probability is 0 to 1%
                             [score: 0.0000]
  1.0 KAM_LAZY_DOMAIN_SECURITY Sending domain does not have any
                             anti-forgery methods
  2.5 KAM_LINKBAIT
           Short messages containing little more than a link, from
                             a domain with no security in place
X-Spam-Flag: NO
X-AntiAbuse: This header was added to track abuse, please include it with any abuse report
X-AntiAbuse: Primary Hostname - vps.ispeakofcake.com
X-AntiAbuse: Original Domain - flynngroup.net
X-AntiAbuse: Originator/Caller UID/GID - [47 12] / [47 12]
X-AntiAbuse: Sender Address Domain - msg.iridium.com
X-Get-Message-Sender-Via: vps.ispeakofcake.com: redirect/forwarder owner adam@flynngroup.net -> adamaflynn@gmail.com
X-Authenticated-Sender: vps.ispeakofcake.com: adam@flynngroup.net
X-Source:
X-Source-Args:
X-Source-Dir:

I am here Lat+37.228828 Lon+26.857672 Alt000ft GPS Sats seen 04 http://map.iridium.com/m?lat=37.128828&lon=26.857672 Sent via Iridium GO!"""
