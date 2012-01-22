%define upstream_name    Text-Patch
%define upstream_version 1.8

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Patches text with given patch
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


