%define upstream_name    Text-Patch
%define upstream_version 1.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Patches text with given patch
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)
BuildArch:	noarch

%description
Text::Patch combines source text with given diff (difference) data. Diff
data is produced by Text::Diff module or by the standard diff utility (man
diff, see -u option).

* patch( $source, $diff, options... )

  First argument is source (original) text. Second is the diff data. Third
  argument can be either hash reference with options or all the rest
  arguments will be considered patch options:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.800.0-4mdv2012.0
+ Revision: 765760
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.800.0-3
+ Revision: 764286
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.800.0-2
+ Revision: 656975
- rebuild for updated spec-helper

* Thu Nov 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.800.0-1mdv2011.0
+ Revision: 596157
- update to 1.8

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 504745
- import perl-Text-Patch


* Fri Feb 12 2010 cpan2dist 1.4-1mdv
- initial mdv release, generated with cpan2dist
