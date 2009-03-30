%undefine __find_provides
%undefine __find_requires

Summary:	Free music files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-moh-freeplay
Version:	20090327
Release:	%mkrel 1
License:	Public Domain
Group:		System/Servers
URL:		http://www.asterisk.org/
Source0:	http://ftp.digium.com/pub/telephony/sounds/%{name}-alaw.tar.gz
Source1:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g722.tar.gz
Source2:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g729.tar.gz
Source3:	http://ftp.digium.com/pub/telephony/sounds/%{name}-gsm.tar.gz
Source4:	http://ftp.digium.com/pub/telephony/sounds/%{name}-siren7.tar.gz
Source5:	http://ftp.digium.com/pub/telephony/sounds/%{name}-siren14.tar.gz
Source6:	http://ftp.digium.com/pub/telephony/sounds/%{name}-sln16.tar.gz
Source7:	http://ftp.digium.com/pub/telephony/sounds/%{name}-ulaw.tar.gz
Source8:	http://ftp.digium.com/pub/telephony/sounds/%{name}-wav.tar.gz
Requires:	asterisk
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable music sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, Siren7, 
Siren14, sln16, mu-Law, WAV

%prep

%setup -q -c -T -n asterisk-moh-freeplay -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/lib/asterisk/sounds

cp -aRf * %{buildroot}/var/lib/asterisk/sounds/

# cleanup
#rm -f %{buildroot}/var/lib/asterisk/sounds/*-asterisk-core-*-%{version}

# make a file list
find %{buildroot}/var/lib/asterisk/sounds -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc *-%{name}-*
