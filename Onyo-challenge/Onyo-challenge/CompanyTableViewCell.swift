//
//  CompanyTableViewCell.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/14/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import UIKit
import AlamofireImage
import MapKit

class CompanyTableViewCell: UITableViewCell {

    @IBOutlet var companyImage: UIImageView!
    @IBOutlet var companyNameDistance: UILabel!
    @IBOutlet var companyAddress: UILabel!
    
    var openMap: (() -> Void)!
    
    let kmToM = 1000
    
    // MARK: - Life Cycle
    
    override func prepareForReuse() {
        companyImage.image = nil
    }
    
    // MARK: - Configure Cell
    
    func configureCellWith(company: Company, indexPath: NSIndexPath, openMap: () -> Void) {
        companyImage.layer.borderColor = UIColor.onyoBlueColor().CGColor
        companyImage.layer.borderWidth = 5.0
        
        if let imageURL = company.imageMainURL {
            companyImage.af_setImageWithURL(NSURL(string: imageURL)!, placeholderImage: nil, filter: AspectScaledToFillSizeFilter(size: companyImage.bounds.size))
        }
        
        companyNameDistance.text = (company.displayName?.uppercaseString)!
        if let latitude = company.addressLatitude.value, let longitude = company.addressLongitude.value {
            let companyLocation = CLLocation(latitude: latitude, longitude: longitude)
            
            if let userLocation = LocationManager.sharedInstance.currentLocation {
                var distance = Int(companyLocation.distanceFromLocation(userLocation))
                
                if distance > kmToM {
                    distance = distance / kmToM
                    let strDistance = distance.description
                    companyNameDistance.text = (company.displayName?.uppercaseString)! + " ~" + strDistance + "km"
                } else {
                    distance = distance / kmToM
                    let strDistance = distance.description
                    companyNameDistance.text = (company.displayName?.uppercaseString)! + " ~" + strDistance + "m"
                }
                
            }
        }
        
        companyAddress.text = company.address?.uppercaseString
        
        if indexPath.row % 2 == 1 {
            backgroundColor = UIColor.onyoGrayColor()
        } else {
            backgroundColor = UIColor.whiteColor()
        }
        
        self.openMap = openMap
        
        layoutIfNeeded()
    }
    
    // MARK: - Actions
    
    @IBAction func goToMap(sender: AnyObject) {
        if let openMapFunction = openMap {
            openMapFunction()
        }
    }
    
}
