Name:		texlive-secdot
Version:	20208
Release:	2
Summary:	Section numbers with trailing dots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/secdot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/secdot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Makes the numbers of \section commands come out with a trailing
dot. Includes a command whereby the same can be made to happen
with other sectioning commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/secdot/secdot.sty
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.ltx
%doc %{_texmfdistdir}/doc/latex/secdot/secdot.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
