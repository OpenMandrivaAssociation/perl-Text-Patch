%define modname	Text-Patch
%define modver 5.13.6

Summary:	Patches text with given patch
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/MIYAGAWA/perl-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Diff)

%description
Text::Patch combines source text with given diff (difference) data. Diff
data is produced by Text::Diff module or by the standard diff utility (man
diff, see -u option).

* patch( $source, $diff, options... )

  First argument is source (original) text. Second is the diff data. Third
  argument can be either hash reference with options or all the rest
  arguments will be considered patch options:

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml ChangeLog
%{perl_vendorlib}/*
%{_mandir}/man3/*


