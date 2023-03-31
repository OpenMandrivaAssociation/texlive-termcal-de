Name:		texlive-termcal-de
Version:	47111
Release:	2
Summary:	German localization for termcal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termcal-de
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal-de.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termcal-de.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a German localization to the termcal
package written by Bill Mitchell, which is intended to print a
term calendar for use in planning a class. termcal-de depends
on the following other packages: termcal, pgfkeys, pgfopts,
datetime2, and datetime2-german.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/termcal-de
%{_texmfdistdir}/tex/latex/termcal-de
%doc %{_texmfdistdir}/doc/latex/termcal-de

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
